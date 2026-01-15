
import os
import random
from tempfile import mkdtemp

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

WAIT_TIMEOUT = 10
SP_UA = (
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) '
    'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.109 Mobile/15E148 Safari/604.1')


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/85.0.4341.72",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/85.0.4341.72",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Vivaldi/5.3.2679.55",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Vivaldi/5.3.2679.55",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Brave/1.40.107",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Brave/1.40.107",
]


class SeleniumUtil:
    def __init__(self):
        self._driver = None

    def build_pc_driver(self):
        options = webdriver.ChromeOptions()

        ua = random.choice(USER_AGENTS)
        options.add_argument(f'--user-agent={ua}')

        self.__build_driver(options)

    def build_sp_driver(self):
        options = webdriver.ChromeOptions()
        # UAをスマホのUAに変更する
        options.add_argument(f'--user-agent={SP_UA}')
        self.__build_driver(options)

    def __build_driver(self, options):

        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--single-process")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-application-cache")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-infobars")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--homedir=/tmp")
        options.add_argument(f"--user-data-dir={mkdtemp()}")
        options.add_argument(f"--data-path={mkdtemp()}")
        options.add_argument(f"--disk-cache-dir={mkdtemp()}")

        # 証明書の警告をOFFにする
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptInsecureCerts'] = True

        # ファイルダウンロードディレクトリ設定、PDFは常にダウンロード設定
        # options.add_experimental_option("prefs", {
        #     "download.default_directory": os.environ['DIR_NAME'],
        #     "plugins.always_open_pdf_externally": True,
        #     "safebrowsing_for_trusted_sources_enabled": False,
        # })

        is_lambda = True
        if os.getenv("IS_DEVCONTAINER", "false") == "true":
            is_lambda = False

        if is_lambda:
            print("running: lambda")
            # ダウンロードしたChromeのファイル指定
            options.binary_location = '/opt/chrome/chrome'
            # ダウンロードしたChromeDriverのファイル指定
            service = webdriver.ChromeService("/opt/chromedriver")
            self._driver = webdriver.Chrome(
                service=service,
                options=options,
            )
        else:
            print("running: devcontainer")
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service

            new_driver = ChromeDriverManager().install()
            service = Service(executable_path=new_driver)
            self._driver = webdriver.Chrome(
                service=service,
                options=options,
            )

        self._driver.set_window_size(950, 800)
        self._driver.set_page_load_timeout(WAIT_TIMEOUT)

        # headlessモードでのファイルダウンロード設定
        # self._driver.command_executor._commands["send_command"] = (
        #     "POST",
        #     '/session/$sessionId/chromium/send_command'
        # )
        # params = {
        #     'cmd': 'Page.setDownloadBehavior',
        #     'params': {
        #         'behavior': 'allow',
        #         'downloadPath': os.environ['DIR_NAME']
        #     }
        # }
        # self._driver.execute("send_command", params=params)

        # waitの初期化
        self._wait = WebDriverWait(self._driver, WAIT_TIMEOUT)

    def driver(self):
        if not self._driver:
            return None

        return self._driver

    def waiter(self):
        return self._wait

    def wait_time(self):
        return WAIT_TIMEOUT

    def dispose_driver(self):
        if not self._driver:
            return

        self._driver.quit()
        self._driver = None

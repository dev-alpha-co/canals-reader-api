from logics.utils.page_base import PageBase
import sys


class CanalsRyokinEditPage(PageBase):
    def __init__(self, selenium, config):
        super().__init__(selenium,
                         url=f'https://{config["CANALS_DOMAIN"]}/admin/CheckRyoukinEdit.jsp')

    # 登録ボタン
    def register_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=confirm]'
        )

    # 送信ボタン
    def submit_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=finish]'
        )

    # 戻るボタン
    def back_button(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[value="料金表一覧に戻る"]'
        )

    # 拠点
    def center_select_box(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'select[name=CenterCD]'
        )

    # 品目名
    def item_name_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=Hinmoku]'
        )

    # 料金
    def charge_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=Ryokin]'
        )

    # 課税区分
    def taxable_radio(self, value='0'):
        return self.create_element(
            sys._getframe().f_code.co_name,
            f'input[name=ZeiKbn][value="{value}"]'
        )

    # 対象時間From
    def time_from_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaishoJikanFrom]'
        )

    # 対象時間To
    def time_to_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaishoJikanTo]'
        )

    # 割増区分
    def warimashi_select_box(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'select[name=HyojiJunjo]'
        )

    # 自動計算フラグ
    def auto_calc_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=AutoCalculationFlag]'
        )

    # 対象時間区分：平日
    def time_kbn_checkbox_weekday(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaishoKbn1]'
        )

    # 対象時間区分：土
    def time_kbn_checkbox_saturday(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaishoKbn2]'
        )

    # 対象時間区分：日・祝
    def time_kbn_checkbox_sunday_holiday(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaishoKbn3]'
        )

    # 最小受注
    def min_order_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=SaisyoJuchu]'
        )

    # 単位数値
    def unit_value_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=Tani]'
        )

    # 単位
    def unit_select_box(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'select[name=TaniKbn]'
        )

    # 単位テキスト
    def unit_text_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=TaniText]'
        )

    # ポイント率
    def point_rate_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=PointRate]'
        )

    # 備考
    def remarks_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'textarea[name=Bikou]'
        )

    # 優待フラグ
    def special_flag_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YutaiFlag]'
        )

    # 勘定科目コード
    def account_code_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=KanjoKamokuCD]'
        )

    # 勘定科目名
    def account_name_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=KanjoKamokuName]'
        )

    # 補助科目コード
    def sub_account_code_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=HojoCode]'
        )

    # 請求方法: 法人
    def billing_method_checkbox_corporate(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=SeikyuHouhou1]'
        )

    # 請求方法: 個人
    def billing_method_checkbox_individual(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=SeikyuHouhou2]'
        )

    # PlanB超過基準時間
    def planb_excess_standard_time_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=ChoukaJikan]'
        )

    # 割引率
    def discount_rate_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=WaribikiPercentage]'
        )

    # 割引フラグ
    def discount_flag_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=WaribikiPercentageFlag]'
        )

    # 法人番号
    def corporate_number_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=HoujinID]'
        )

    # キャンセルフィー:　前日
    def cancel_fee_checkbox_before_day(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=IncludedInPrecedingDayCancel]'
        )

    # キャンセルフィー: 当日
    def cancel_fee_checkbox_on_day(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=IncludedInAppointedDayCancel]'
        )

    # 表示優先度
    def display_priority_input(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=DisplayPriority]'
        )

    # 定率割引フラグ
    def flat_rate_discount_flag_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=IncludedInWaribikiTargets]'
        )

    # 品目区分
    def item_kbn_radio(self, value='0'):
        return self.create_element(
            sys._getframe().f_code.co_name,
            f'input[name=HinmokuKbn][value="{value}"]'
        )

    # 品目区分2
    def item_kbn2_radio(self, value='0'):
        return self.create_element(
            sys._getframe().f_code.co_name,
            f'input[name=HinmokuKbn2][value="{value}"]'
        )

    # 使用区分
    # 入会金
    def entrance_fee_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=NyukaikinFlag]'
        )

    # 年会費
    def annual_fee_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=NenkaihiFlag]'
        )

    # 受注・前受 デイケア
    def order_prepay_daycare_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JuchuDaycareFlag]'
        )

    # 受注・前受 教室
    def order_prepay_classroom_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JuchuKyoushitsuFlag]'
        )

    # 受注・前受 AKC
    def order_prepay_akc_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JuchuAKCFlag]'
        )

    # 受注・前受 バックアップ
    def order_prepay_backup_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JuchuPlanBFlag]'
        )

    # 初回請求分
    def first_billing_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=ShokaiSeikyuFlag]'
        )

    # 予約 デイケア
    def reservation_daycare_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuDaycareAddFlag]'
        )

    # 予約 デイケア日数追加
    def reservation_daycare_days_add_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuDaycareNissuAddFlag]'
        )

    # 予約 教室日数追加
    def reservation_classroom_days_add_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuKyoushitsuNissuAddFlag]'
        )

    # 予約 教室
    def reservation_classroom_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuKyoushitsuAddFlag]'
        )

    # 予約 一時預かり/ホテル託児
    def reservation_temporary_care_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuKSFlag]'
        )

    # 予約 AKC
    def reservation_akc_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuAKCFlag]'
        )

    # 予約 バックアップ
    def reservation_backup_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuPlanBFlag]'
        )

    # 予約 劇団四季
    def reservation_gekidan_shiki_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuGekidanShikiFlag]'
        )

    # 予約 宴会イベント
    def reservation_banquet_event_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuEnkaiEventFlag]'
        )

    # 予約 家事代行
    def reservation_housekeeping_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=YoyakuKajiDaikoFlag]'
        )

    # 実施 デイケア
    def implementation_daycare_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiDaycareAddFlag]'
        )

    # 実施 デイケア日数追加
    def implementation_daycare_days_add_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiDaycareNissuAddFlag]'
        )

    # 実施 教室日数追加
    def implementation_classroom_days_add_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiKyoushitsuNissuAddFlag]'
        )

    # 実施 教室
    def implementation_classroom_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiKyoushitsuAddFlag]'
        )

    # 実施 一時預かり/ホテル託児
    def implementation_temporary_care_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiKSFlag]'
        )

    # 実施 AKC
    def implementation_akc_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiAKCFlag]'
        )

    # 実施 バックアップ
    def implementation_backup_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiPlanBFlag]'
        )

    # 実施 劇団四季
    def implementation_gekidan_shiki_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiGekidanShikiFlag]'
        )

    # 実施 宴会イベント
    def implementation_banquet_event_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiEnkaiEventFlag]'
        )

    # 実施 家事代行
    def implementation_housekeeping_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JisshiKajiDaikoFlag]'
        )

    # 割引チケット
    def discount_ticket_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=JIsshiWaribikiFlag]'
        )

    # 顧客区分
    # プレミア
    def customer_kbn_premium_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn1]'
        )

    # ビジター
    def customer_kbn_visitor_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn2]'
        )

    # 法人メンバー
    def customer_kbn_corporate_member_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn3]'
        )

    # 支店会員
    def customer_kbn_branch_member_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn4]'
        )

    # 法人
    def customer_kbn_corporate_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn5]'
        )

    # BS会員
    def customer_kbn_bs_member_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn6]'
        )

    # 優待会員
    def customer_kbn_special_member_checkbox(self):
        return self.create_element(
            sys._getframe().f_code.co_name,
            'input[name=MemberKbn7]'
        )

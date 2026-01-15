# ECRの初期設定
- リポジトリ作成
FUNCTION_NAME="xxxx"
aws ecr create-repository --repository-name $FUNCTION_NAME
ex)aws ecr create-repository --repository-name check-notifier | jq

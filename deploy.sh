#!/bin/bash

set -eu
# usage
cmdname=`basename $0`
function usage()
{
  echo "Usage: ${cmdname} env" 1>&2
  echo 'env: "dev" or "prod"' 1>&2
  return 0
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

ENV=$1
FUNCTION_NAME="check-notifier"
AWS_ACCOUNT_ID=015488197376
AWS_REGION=ap-northeast-1
ECR_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$FUNCTION_NAME:latest

# コンテナビルド
docker build -t $FUNCTION_NAME .
docker tag $FUNCTION_NAME:latest $ECR_URI

# コンテナ更新
aws ecr get-login-password \
  | docker login \
    --username AWS \
    --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker push $ECR_URI

# Lambdaへデプロイ
aws lambda update-function-code \
  --function-name $FUNCTION_NAME \
  --image-uri $ECR_URI | jq
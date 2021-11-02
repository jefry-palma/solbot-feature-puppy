time_stamp=$(date +"%b_%d_%Y_%H_%M_%S")
artifact_name=s3://jpalmasolutions/zip/solbot_puppy_feature/$time_stamp.zip
pipenv lock -r > requirements.txt
pip3 install -r requirements.txt --no-deps -t lambda
mkdir lambda/src
cp -r src/* lambda/src/
cd lambda
zip -r lambda.zip *
mv lambda.zip ..
cd ..
rm requirements.txt
aws s3 cp lambda.zip $artifact_name
rm lambda.zip
rm -r lambda
echo $artifact_name
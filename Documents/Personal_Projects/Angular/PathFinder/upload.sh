ng build
aws s3 rm s3://pathfind.com --recursive
aws s3 sync ./dist/ s3://pathfind.com --acl public-read
#aws cloudfront create-invalidation --distribution-id EO37R0PS8J6V4 --paths "/*"



import boto3




def lambda_handler(event, context):
  
  
  
  tagged_now = 0
  cant_tag   = 0
  alrdy_tagged =0
  all_ebs_count = 0
  
  
  regions = ["eu-west-1","eu-west-2","us-east-1","us-east-2"]
  #remove ,"us-east-2" when in LE accounts
  
  tagged_now = 0
  cant_tag   = 0
  alrdy_tagged =0
  all_cloudwatch_count = 0
  
  for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    volumes = ec2.volumes.all() # If you want to list out all volumes
    
    for volume in volumes :
      all_ebs_count += 1
      flag = 0 
      tags_in_ebs = (volume.tags)
      try:
        for tag in tags_in_ebs:
          if (tag['Key'] == 'abcd'  ):
            flag = 1 
            
            alrdy_tagged += 1
            
          #print(tag)

        
      except Exception as e:
        print(e) 
        
      if ( flag == 0  ):
        try:
          volume.create_tags(Tags=[{'Key': 'abcd', 'Value': 'abcd'  }])
          tagged_now +=1

        except Exception as e:
          print (e)
          cant_tag += 1
        
        
  print('all cloud watch  count',all_ebs_count)
  print('already tagged count' ,alrdy_tagged )
  print('tagged from this attempt',tagged_now)
  print('refused to tag',cant_tag )
      
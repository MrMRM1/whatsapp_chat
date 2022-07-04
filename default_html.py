head_html = ('''

<!DOCTYPE html>
<html>

 <head>

  <meta charset="utf-8"/>
<title>Exported Data</title>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>

  <style>
    body {
    margin: 0;
    font: 14px/18px 'Open Sans',"Lucida Grande","Lucida Sans Unicode",Arial,Helvetica,Verdana,sans-serif;
}
.clearfix:after {
    content: " ";
    visibility: hidden;
    display: block;
    height: 0;
    clear: both;
}
.pull_left {
    float: left;
}
.pull_right {
    float: right;
}
.page_wrap {
    background-color: #ffffff;
    color: #000000;
}
.page_wrap a {
    color: #168acd;
    text-decoration: none;
}

.page_header {
    /*position: fixed;*/
    z-index: 10;
    background-color: #ffffff;
    width: 100%;
    border-bottom: 1px solid #e3e6e8;
}
.page_header .content {
    width: 480px;
    margin: 0 auto;
    border-radius: 0 !important;
}
.page_header a.content {
    background-repeat: no-repeat;
    background-position: 24px 21px;
    background-size: 24px 24px;
}
.bold {
    color: #212121;
    font-weight: 700;	
}
.details {
    color: #000000;
}

.page_header .content .text {
    padding: 24px 24px 22px 24px;
    font-size: 22px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
text-align:center
}
.page_header a.content .text {
    padding: 24px 24px 22px 82px;
}
.page_body {
    padding-top: 64px;
    width: 480px;
    margin: 0 auto;
}

.userpic {
    display: block;
    border-radius: 50%;
    overflow: hidden;
}
.userpic .initials {
    display: block;
    color: #fff;
    text-align: center;
    text-transform: uppercase;
    user-select: none;
}

.color_green,
.userpic2,
.media_call.success .fill,
.media_photo .fill {
    background-color: #64bf47;
}


a.block_link {
    display: block;
    text-decoration: none !important;
    border-radius: 4px;
}

.history {
    padding: 16px 0;
}
.message {
    margin: 0 -10px;
    transition: background-color 2.0s ease;
}

.service {
    padding: 10px 24px;
}
.service .body {
    text-align: center;
}
.message .userpic .initials {
    font-size: 16px;
}
.default {
    padding: 10px;
}

.default .from_name {
    color: #3892db;
    font-weight: 700;
    padding-bottom: 5px;
}
.default .from_name .details {
    font-weight: normal;
}
.default .body {
    margin-left: 60px;
}
.default .text {
    word-wrap: break-word;
    line-height: 150%;
}






  </style>


 </head>

 <body onload="CheckLocation();">

  <div class="page_wrap">

   <div class="page_header">

    <a class="content block_link" href="http://mrmrm.ir/" onclick="return GoBack(this)">

     <div class="text bold">
Whatsapp chat
     </div>

    </a>

   </div>

   <div class="page_body chat_page">

    <div class="history">




''')


def message_html(user, datatime, time, massage_text):
    return ('''<div class="message default clearfix">

      <div class="pull_left userpic_wrap">

       <div class="userpic userpic2" style="width: 42px; height: 42px">

        <div class="initials" style="line-height: 42px">
{}
        </div>

       </div>

      </div>

      <div class="body">

       <div class="pull_right date details" title="{}">
{}
       </div>

       <div class="from_name">
{}
       </div>

       <div class="text">
{}
       </div>

      </div>

     </div>'''.format(user[0:2], datatime, time, user, massage_text))


def continue_message(massage_text):
    return '''<div class="message default clearfix joined">

      <div class="body">

       <div class="pull_right date details" title="">
       </div>

       

       <div class="text">
{}
       </div>

      </div>

     </div>'''.format(massage_text)


def message_service(message):
    return '''<div class="message service">

      <div class="body details">
{}
      </div>

     </div>'''.format(message)


def footer_html():
    return '''

</div>
   </div>

  </div>

 </body>

</html>
'''
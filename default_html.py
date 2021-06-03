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
strong {
    font-weight: 700;
}
code, kbd, pre, samp {
    font-family: Menlo,Monaco,Consolas,"Courier New",monospace;
}
code {
    padding: 2px 4px;
    font-size: 90%;
    color: #c7254e;
    background-color: #f9f2f4;
    border-radius: 4px;
}
pre {
    display: block;
    margin: 0;
    line-height: 1.42857143;
    word-break: break-all;
    word-wrap: break-word;
    color: #333;
    background-color: #f5f5f5;
    border-radius: 4px;
    overflow: auto;
    padding: 3px;
    border: 1px solid #eee;
    max-height: none;
    font-size: inherit;
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
.page_wrap a:hover {
    text-decoration: underline;
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
.details1 {
    color: #000000;
font-weight : 900;
font-family: tahoma;
direction: rtl;
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
.page_about {
    padding: 24px 24px;
}
.with_divider {
    border-top: 1px solid #e3e6e8;
}
.userpic_link {
    display: block;
    text-decoration: none;
}
.userpic_link:hover {
    text-decoration: none;
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
.color_red,
.userpic1,
.media_call .fill,
.media_file .fill,
.media_live_location .fill {
    background-color: #ff5555;
}
.color_green,
.userpic2,
.media_call.success .fill,
.media_photo .fill {
    background-color: #64bf47;
}
.color_yellow,
.userpic3,
.media_venue .fill {
    background-color: #ffab00;
}
.color_blue,
.userpic4,
.media_audio_file .fill,
.media_voice_message .fill {
    background-color: #4f9cd9;
}
.color_purple,
.userpic5,
.media_game .fill {
    background-color: #9884e8;
}
.color_pink,
.userpic6,
.media_invoice .fill {
    background-color: #e671a5;
}
.color_sea,
.userpic7,
.media_location .fill,
.media_video .fill {
    background-color: #47bcd1;
}
.color_orange,
.userpic8,
.media_contact .fill {
    background-color: #ff8c44;
}
.personal_info {
    padding: 24px;
}
.personal_info .userpic .initials {
    font-size: 30px;
}
.personal_info .rows {
    float: left;
    padding-right: 24px;
}
.personal_info .names {
    width: 164px;
}
.personal_info .info {
    width: 124px;
}
.personal_info .bio {
    width: 400px;
}
.personal_info .row {
    padding-bottom: 16px;
}
a.block_link {
    display: block;
    text-decoration: none !important;
    border-radius: 4px;
}
a.block_link:hover {
    text-decoration: none !important;
    background-color: #f5f7f8;
}
.sections {
    padding: 11px 0;
}
.section {
    height: 48px;
    background-position: 24px 12px;
    background-repeat: no-repeat;
    background-size: 24px 24px;
}
.section .counter {
    float: right;
    padding: 14px 24px 0;
    font-size: 15px;
}
.section .label {
    padding: 15px 0 0 82px;
    font-size: 15px;
}
.list_page .page_about {
    padding: 16px 24px 0;
    font-size: 11px;
color: #000000;
font-weight : 900;
font-family: tahoma;
text-align: center;
}
.list_page .entry_list {
    padding: 16px 0;
}
.list_page .entry {
    padding: 10px 16px;
}
.list_page .entry .userpic .initials {
    font-size: 18px;
}
.list_page .entry .body {
    margin-left: 66px;
}
.list_page .entry .name {
    padding: 4px 0 2px;
    font-size: 14px;
}
.list_page .entry .subname {
    padding-top: 4px;
}
.list_page .entry .details_entry {
    padding-top: 4px;
}
.list_page .entry .info {
    font-size: 11px;
    padding-top: 5px;
}
.history {
    padding: 16px 0;
}
.message {
    margin: 0 -10px;
    transition: background-color 2.0s ease;
}
div.selected {
    background-color: rgba(242,246,250,255);
    transition: background-color 0.5s ease;
}
.service {
    padding: 10px 24px;
}
.service .body {
    text-align: center;
}
.service .userpic_wrap {
    padding-top: 10px;
}
.service .userpic {
    margin: 0 auto;
}
.service .userpic .initials {
    font-size: 24px;
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


def massage_html(user, data, massage_text):
    return ('''

                         <div class="message default clearfix" id="message13085">

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

                     </div>

                        '''.format(user, data[0], data[1], data[3], massage_text))


def continue_massage(massage_text):
    return '''
                                     <div class="message default clearfix" id="message13085">

                      <div class="body">

                       <div class="text">
                {}
                       </div>
    
                      </div>
    
                     </div>
                                    '''.format(massage_text)


def footer_html():
    return '''

</div>
   <a class="content block_link" href="http://mrmrm.ir/" onclick="return GoBack(this)">

     <div class="text bold">
by Mohammad Reza Mehrabany
     </div>

    </a>
   </div>

  </div>

 </body>

</html>



'''
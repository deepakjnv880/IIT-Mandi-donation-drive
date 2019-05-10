// <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
// var socket = io.connect('http://' + document.domain + ':' + location.port);
//
// socket.on('connect', function() {
//   alert("inbuild or io.connect => conenction");
//   var myemail=document.getElementById('trick');
//   // alert(myemail.value);
//   socket.emit("makeroom",{me:myemail.value});
//   socket.emit('online',{me:myemail.value});
//   // socket.emit('update_post');
//   // update_post();
// //     // socket.emit('connection', {data: 'I\'m connected!'});
// });
// function update_post() {
//   alert("yoyoyo0");
 socket.emit('update_post');
// // var socket = io.connect('http://' + document.domain + ':' + location.port);
//  socket.on('update_post', function(data) {
//    alert("i am in");
//        // alert(data['did']);
//    if (data['dtype']==="daily_use_item") {
//          var div = document.createElement("div");
//          div.style.width = "55vw";
//          // div.style.height = auto;
//          div.style.border = "1px solid black";
//          div.style.borderRadius = "5px";
//          div.style.background = "white";
//          div.style.margin="10px";
//          var creater = document.createElement("P");
//          creater.innerHTML=data['pemail'];
//          var str = data['pemail'];
//          var res = str.toUpperCase();
//          creater.innerHTML=res;
//          creater.className="make_bold make_italic";
//          creater.innerHTML+='<button style="float:right;text-decoration:none;background-color:blue; color:white" disabled>PERSON</button>';
//          creater.style.color="red";
//          div.appendChild(creater);
//          div.innerHTML += data['time'];
//          div.innerHTML+="<br>";
//          div.innerHTML+="<br>";
//          div.innerHTML += data['post'];
//          div.innerHTML+="<br>";
//          if (data['filename']) {
//            div.innerHTML+="<img src=\"http://localhost:5000/uploads/"+data['filename']+"\" width=\"714px\" >";
//          }
//          var lower=document.createElement("div");
//          var b1=document.createElement("button");
//          b1.className = "fas fa-thumbs-up recommended";
//          b1.innerHTML+=" RECOMMENDED";
//          b1.style.width = "17vw";
//          b1.style.height = "3vw";
//          b1.style.margin="2px";
//          b1.onclick = function(){
//            if (b1.style.backgroundColor=='') {
//                b1.style.backgroundColor='aqua';
//                b2.style.backgroundColor='';
//            }
//            else {
//              b1.style.backgroundColor='';
//            }
//          };
//          lower.appendChild(b1);
//          var b2=document.createElement("button");
//          b2.className = "fas fa-thumbs-down not_recommended";
//          b2.innerHTML+=" NOT RECOMMENDED";
//          b2.style.width = "18vw";
//          b2.style.height = "3vw";
//          b2.style.margin="2px";
//          b2.onclick = function(){
//            if (b2.style.backgroundColor=='') {
//                b2.style.backgroundColor='red';
//                b1.style.backgroundColor='';
//            }
//            else {
//              b2.style.backgroundColor='';
//            }
//          };
//          lower.appendChild(b2);
//          var b3=document.createElement("button");
//          b3.className = "fas fa-comment comment";
//          b3.innerHTML+=" COMMENT"
//          b3.style.width = "17vw";
//          b3.style.height = "3vw";
//          b3.style.margin="2px";
//          lower.appendChild(b3);
//
//          var b4=document.createElement("textarea");
//          b4.ID = "create_comment";
//          b4.placeholder=" Write a comment...";
//          b4.cols = 72;
//          b4.rows = 1;
//          b4.style.resize='none';
//          b4.style.margin="2px";
//          lower.appendChild(b4);
//
//          var b5=document.createElement("button");
//          // b5.className = "fas fa-comment comment";
//          b5.innerHTML="POST";
//          b5.style.cssFloat = "right";
//          b5.style.marginRight="25px";
//          // b5.style.height = "3vw";
//          // b5.style.margin="2px";
//          lower.appendChild(b5);
//
//
//          lower.style.border = "1px solid black";
//          // lower.style.borderRadius = "5px";
//          var commentdiv=document.createElement("div");
//          commentdiv.style.width = "48vw";
//          commentdiv.style.height = "18vw";
//          commentdiv.style.display='none';
//          commentdiv.innerHTML = "HI deepak here u can post your comment";
//          b3.onclick = function(){
//
//
//            if (commentdiv.style.display=='none') {
//              // alert(commentdiv.style.display);
//              commentdiv.style.display='block';
//              lower.appendChild(commentdiv);
//            }
//            else {
//              commentdiv.style.display='none';
//            }
//          };
//          div.appendChild(lower);
//          document.getElementById("read_post").appendChild(div);
//    }
//    else if (data['dtype']==="social") {
//      var div = document.createElement("div");
//      div.style.width = "55vw";
//      // div.style.height = auto;
//      div.style.border = "1px solid black";
//      div.style.borderRadius = "5px";
//      div.style.background = "white";
//      div.style.margin="10px";
//      var creater = document.createElement("P");
//      var str = data['cemail'];
//      var res = str.toUpperCase();
//      creater.innerHTML=res;
//      creater.className="make_bold make_italic";
//      creater.innerHTML+='<button style="float:right;text-decoration:none;background-color:blue; color:white" disabled>SOCIAL</button>';
//      creater.style.color="red";
//      div.appendChild(creater);
//      div.innerHTML += data['time'];
//      div.innerHTML+="<br>";
//      div.innerHTML+="<br>";
//      div.innerHTML += data['post'];
//      div.innerHTML+="<br>";
//      if (data['filename']) {
//        div.innerHTML+="<img src=\"http://localhost:5000/uploads/"+data['filename']+"\" width=\"714px\" >";
//      }
//      var lower=document.createElement("div");
//      var b1=document.createElement("button");
//      b1.className = "fas fa-thumbs-up recommended";
//      b1.innerHTML+=" INTERESTED";
//      b1.style.width = "17vw";
//      b1.style.height = "3vw";
//      b1.style.margin="2px";
//      b1.onclick = function(){
//        if (b1.style.backgroundColor=='') {
//            b1.style.backgroundColor='aqua';
//            b2.style.backgroundColor='';
//        }
//        else {
//          b1.style.backgroundColor='';
//        }
//      };
//      lower.appendChild(b1);
//      var b2=document.createElement("button");
//      b2.className = "fas fa-thumbs-down not_recommended";
//      b2.innerHTML+=" NOT INTERESTED";
//      b2.style.width = "18vw";
//      b2.style.height = "3vw";
//      b2.style.margin="2px";
//      b2.onclick = function(){
//        if (b2.style.backgroundColor=='') {
//            b2.style.backgroundColor='red';
//            b1.style.backgroundColor='';
//        }
//        else {
//          b2.style.backgroundColor='';
//        }
//      };
//      lower.appendChild(b2);
//      var b3=document.createElement("button");
//      b3.className = "fas fa-comment comment";
//      b3.innerHTML+=" COMMENT"
//      b3.style.width = "17vw";
//      b3.style.height = "3vw";
//      b3.style.margin="2px";
//      lower.appendChild(b3);
//
//      var b4=document.createElement("textarea");
//      b4.ID = "create_comment";
//      b4.placeholder=" Write a comment...";
//      b4.cols = 72;
//      b4.rows = 1;
//      b4.style.resize='none';
//      b4.style.margin="2px";
//      lower.appendChild(b4);
//
//      var b5=document.createElement("button");
//      // b5.className = "fas fa-comment comment";
//      b5.innerHTML="POST";
//      b5.style.cssFloat = "right";
//      b5.style.marginRight="25px";
//      // b5.style.height = "3vw";
//      // b5.style.margin="2px";
//      lower.appendChild(b5);
//
//
//      lower.style.border = "1px solid black";
//      // lower.style.borderRadius = "5px";
//      var commentdiv=document.createElement("div");
//      commentdiv.style.width = "48vw";
//      commentdiv.style.height = "18vw";
//      commentdiv.style.display='none';
//      commentdiv.innerHTML = "HI deepak here u can post your comment";
//      b3.onclick = function(){
//
//
//        if (commentdiv.style.display=='none') {
//          // alert(commentdiv.style.display);
//          commentdiv.style.display='block';
//          lower.appendChild(commentdiv);
//        }
//        else {
//          commentdiv.style.display='none';
//        }
//      };
//      div.appendChild(lower);
//      document.getElementById("read_post").appendChild(div);
//    }
//    else if (data['dtype']==="club_requirement") {
//      var div = document.createElement("div");
//      div.style.width = "55vw";
//      // div.style.height = auto;
//      div.style.border = "1px solid black";
//      div.style.borderRadius = "5px";
//      div.style.background = "white";
//      div.style.margin="10px";
//      var creater = document.createElement("P");
//      var str = data['cemail'];
//      var res = str.toUpperCase();
//      creater.innerHTML=res;
//      creater.className="make_bold make_italic";
//      creater.innerHTML+='<button style="float:right;text-decoration:none;background-color:blue; color:white" disabled>CLUB</button>';
//      creater.style.color="red";
//      div.appendChild(creater);
//      div.innerHTML += data['time'];
//      div.innerHTML+="<br>";
//      div.innerHTML+="<br>";
//      div.innerHTML += data['post'];
//      div.innerHTML+="<br>";
//      if (data['filename']) {
//        div.innerHTML+="<img src=\"http://localhost:5000/uploads/"+data['filename']+"\" width=\"714px\" >";
//      }
//      var lower=document.createElement("div");
//      var b1=document.createElement("button");
//      b1.className = "fas fa-thumbs-up recommended";
//      b1.innerHTML+=" INTERESTED";
//      b1.style.width = "17vw";
//      b1.style.height = "3vw";
//      b1.style.margin="2px";
//      b1.onclick = function(){
//        alert(data['did']);
//        if (b1.style.backgroundColor=='') {
//            b1.style.backgroundColor='aqua';
//            b2.style.backgroundColor='';
//        }
//        else {
//          b1.style.backgroundColor='';
//        }
//      };
//      lower.appendChild(b1);
//      var b2=document.createElement("button");
//      b2.className = "fas fa-hand-holding-usd not_recommended";
//      b2.innerHTML+=" Donate";
//      b2.style.width = "18vw";
//      b2.style.height = "3vw";
//      b2.style.margin="2px";
//      b2.onclick = function(){
//        if (b2.style.backgroundColor=='') {
//            b2.style.backgroundColor='red';
//            b1.style.backgroundColor='';
//        }
//        else {
//          b2.style.backgroundColor='';
//        }
//      };
//      lower.appendChild(b2);
//
//      var b3=document.createElement("button");
//      b3.className = "fas fa-comment comment";
//      b3.innerHTML+=" COMMENT";
//      b3.style.width = "17vw";
//      b3.style.height = "3vw";
//      b3.style.margin="2px";
//      lower.appendChild(b3);
//
//      var b4=document.createElement("textarea");
//      b4.ID = "create_comment";
//      b4.placeholder=" Write a comment...";
//      b4.cols = 72;
//      b4.rows = 1;
//      b4.style.resize='none';
//      b4.style.margin="2px";
//      lower.appendChild(b4);
//
//      var b5=document.createElement("button");
//      // b5.className = "fas fa-comment comment";
//      b5.innerHTML="POST";
//      b5.style.cssFloat = "right";
//      b5.style.marginRight="25px";
//      // b5.style.height = "3vw";
//      // b5.style.margin="2px";
//      lower.appendChild(b5);
//
//      lower.style.border = "1px solid black";
//      // lower.style.borderRadius = "5px";
//      var commentdiv=document.createElement("div");
//      commentdiv.style.width = "48vw";
//      commentdiv.style.height = "18vw";
//      commentdiv.style.display='none';
//      commentdiv.innerHTML = "HI deepak here u can post your comment";
//      b3.onclick = function(){
//
//
//        if (commentdiv.style.display=='none') {
//          // alert(commentdiv.style.display);
//          commentdiv.style.display='block';
//          lower.appendChild(commentdiv);
//        }
//        else {
//          commentdiv.style.display='none';
//        }
//      };
//      div.appendChild(lower);
//      document.getElementById("read_post").appendChild(div);
//    }
//  });
// }
//
//   // <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
// // var socket = io.connect('http://' + document.domain + ':' + location.port);
// // function die() {
//
//
// // }
// //

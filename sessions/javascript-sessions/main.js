var count = 1
function guess(){
     const LUCKY_NUMBER = 7
     var guessedNumber = $("#num").val()
     if(guessedNumber > 10 || guessedNumber < 1 ){
          alert("Number should be between 1 to 10")
     }
     else{
          if(guessedNumber == LUCKY_NUMBER){
               $("#result").html("Congrats!! You guessed it right in "+count +" attempts")
          }
          else{
               $("#result").html("Try Again!! Better luck next time")
               count+
          }
     }
}

$("p").click(function()=> alert("paragraph clicked")
)



//function greet(){
   //  let username =Number(document.getElementById("userId").value)
     /*let num= 10;*/
   //  alert(typeof username)
     /*alert(username)*/
  //   document.getElementById("value").innerHTML="CONGRATULATIONS  "   +username+"!!"
     /*document.write(username)*/
    ///// document.getElementById(userId).value = ""
     
//}


///function add(){



//}

//let a=10
//let b=10
//console.log(a+b)

//console.log("Welcome");//


//function promptDemo(){
   //  let employee = prompt("Please enter your name", "John")
    // if(employee != null $$ employee ! = ""){
   //       alert(employee)
  //   }{
  //        alert(employee)
  //   }
   //  else{
  ///        alert("Incorrect Employee")
   //  }
     
     
//}
//function confirmmDemo(){
   //  let text=Press = "Press OK or Cancel"
   //  if(confirm(text) == true) {
   //       alert("OK")
   //  }
   //////  else{
    //      alert("Cancel")
   //  }

//}


/* 
(username)Variable: Named storage- the value is storred in the variable:username

DATA TYPE:
 -string(all text,words, characters)
 -number(intereger)
 booleanb(*true,false)
 -object
 -Arrays(group of data)
           -String
                10 + 43 = 1043
           -Number
                 10 + 43 = 53- it will do the math
 -undefined data: null, 0, infinity.

*/


/* in every application will have:   
        C - Create
        R - Read
        U - Update
        D - Delete



*/



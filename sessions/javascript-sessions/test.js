/*var a = 10
var a = 30*/
/*let a = 10
let a = 30*error*/ 
//let a = 10 //Redeclaration is restricted
//a = 30 //reassigment
//console.log(a)

// let name1 = 'John'// declaration
//let name1 = "John"//Defined
//console.log(name1) 
//alert(1)// alert box only in browser

 //let num1= "10"
 // console.log(typeof num1) string
 //console.log(num1/2)  number/

 //let result = num1/"5"
 //console.log(typeof result)number

 //let nume1 = "ten10"
 //let result = num1/"5"
 //console.log(result)
 //console.log(Boolean("")) 0,null, empty strings=false
//num1++
 //console.log(num1++) //12 Post increment
 //console.log(num1)

 //console.log(++num1) //Pre increment

 //let num2 = 10

 //console.log(num1 == num2) false

 //console.log(num1=== num2) //strict comparison 3x=  : compare along with data trype.

 //console.log(num1 == num2 || num>num2) strict comparison
    //if(num1 >= 10){
   // console.log("Greater than ten") //not,  >= greater than ten 
    //}
   //else{
   //  console.log("Not greater than ten")
//} 

// num1 > 10 ? console.log("greater than 10") : console.log("not greater than 10")          not > 10

//Print table of 2:
//console.log(2*1)
//console.log(2*2)


   //let i = 1 //initialization
   //while(i<=10){  //Condition
    //console.log(2*1)         
   // i++ //Increment
    //}

  // for (var counter = 1; counter < 5; counter++) {
  //   console.log('Inside the loop:' + counter);
  // } console.log('Outside the loop:' + counter);    1. true

   
// create a loop and display the even numbers till 100



 let names = ["Sam","Liam","Vince","Azhar"]



 for(let name of names){  //of for string   in for value-0 1 2 3 
  // console.log(name)

 }

 names.length = 2  //reduces the size of array
 //console.log(names)
 names.length = 4
 //console.log(names)  // 2 empty items-lost the last 2 names


// console.log(names.length)
//console.log(names[1])

//access last element
//console.log(names[names.length-1])
//console.log("Original Array:")
//console.log(names)    //shows the array
//console.pop()
//console.log("Modified Array after pop:")
//console.log(names)

//names.push("Michelle")
//console.log("Modified Array after push:")
//console.log(names)
//names[2] = "Florina"
//names[10] = "Asiya"
//console.log(names.length)
//console.log("Modified Array")
//console.log(names)



//let m = [10, 20]
//catchM(m)
//console.log(m)

function catchM(n){
             // add value to an array
   
}
 let arr = [12,8,24,13,15,7]
 let evenNumbers = arr.filter(myFunction)  //Callback function
 console.log(evenNumbers)
 function myFunction(n){
   return n%2 == 0

 }












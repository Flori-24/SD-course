const posts = []
let currentPostIndex = null

document.getElementById('doctorForm').addEventListener('submit', (e)=>{
    e.preventDefault();
    const title = document.getElementById('title').value
    const ailment = document.getElementById('ailment').value
    const futureDate = document.getElementById('futureDate').value
    const appTime = document.getElementById('appTime').value
    const comments = document.getElementById('comments').value



    if(currentPostIndex !== null){
      posts[currentPostIndex] = {title, ailment, futureDate, appTime, comments}
    
      currentPostIndex = null;
    }
    else{
        posts.push({title, ailment, futureDate, appTime, comments} )
     
    }
    //addPost(title, ailment, futureDate, appTime, comments)
    renderPost()
    document.getElementById('doctorForm').reset()
})

//function addPost(title, ailment, futureDate, appTime, comments){
   // let postContainer  = document.getElementById('posts')
    //let postElement = document.createElement('div')
   // postElement.className = 'card mb-3'
   // postElement.innerHTML = `
    //     <div class= 'card-body'>
     //    <h6 class= "card-title">Name: ${title}</h5>
      //   <p class="card-ailment">Type of ailment: ${ailment}</p>
      //   <p class="card-futureDate">Appoinment Date: ${futureDate}</p>
       //  <p class="card-appTime">Appoinment Time: ${appTime}</p>
       //  <p class="card-comments">Comments: ${comments}</p>
       //  <button type="button" class="btn btn-secondary" onclick="editPost(${posts.length - 1})">Edit</button>
       //  <button type="button" class="btn btn-danger" onclick="deletePost(${posts.length - 1})">Delete</button>
  //  `
  //  postContainer.appendChild(postElement)
//}


const today = new Date();
const formatToday = today.toISOString().split('T')[0];


const maxDate = new Date();
maxDate.setDate(today.getDate() + 15);
const formatMaxDate = maxDate.toISOString().split('T')[0];

const appointmentDateInput = document.getElementById('futureDate');
appointmentDateInput.setAttribute("min", formatToday);
appointmentDateInput.setAttribute("max", formatMaxDate);



function renderPost(){
    let postContainer = document.getElementById('posts')
    postContainer.innerHTML = ''

    posts.forEach((post, index)=>{
        let postElement = document.createElement('div')
        postElement.className = 'card mb-3'

        postElement.innerHTML = `
          <div class= 'card-body'>
             <h6 class= "card-title">Name: ${post.title}</h6>
             <p class="card-ailment">Type of ailment: ${post.ailment}</p>
             <p class="card-futureDate">Appointment Date: ${post.futureDate}</p>
             <p class="card-appTime">Appointment Time: ${post.appTime}</p>
             <p class="card-comments">Comments: ${post.comments}</p>
             <button type="button" class="btn btn-secondary" onclick="editPost(${index})">Edit</button>
             <button type="button" class="btn btn-danger" onclick="deletePost(${index})">Delete</button>
          </div>
         `
         postContainer.appendChild(postElement)

    })  
}
function editPost(index){

  currentPostIndex = index
 

  document.getElementById('title').value = posts[index].title
  document.getElementById('ailment').value = posts[index].ailment
  document.getElementById('futureDate').value = posts[index].futureDate
  document.getElementById('appTime').value = posts[index].appTime
  document.getElementById('comments').value = posts[index].comments

  

}
function deletePost(index){
  posts.splice(index, 1)
  renderPost()
}


// online doctor appointment app
// Name: textbox
// Ailment: dropdown
// Date-time: Datepicker (you can only select future date)
// comments: textarea

// Button: Book an appointment
// Button: Edit
// Button: Delete
 

// This function will get the faculty names based on the
// course selection
function get_faculty_names() {

    var course = document.getElementById("i3").value;
    course = 'course_name='+course;

    var request = new XMLHttpRequest(); // creating object to XMLHttpRequest class
    request.onreadystatechange = show_faculty;
    request.open("POST","http://127.0.0.1:8000/faculty_names/",true);
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    request.send(course);

    function show_faculty()
    {
       if(request.readyState == 4)
       {
           // reading response text
           var response_text = request.responseText;

           // Converting response texts
           var json_object = JSON.parse(response_text);

           var json_keys_length = Object.keys(json_object).length;

           for(var i=1; i <= json_keys_length; i++)
           {
               alert(json_object)
           }
       }
    }
}

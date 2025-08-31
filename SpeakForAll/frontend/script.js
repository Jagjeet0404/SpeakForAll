async function processText(){
  let text = document.getElementById("inputText").value;
  let formData = new FormData();
  formData.append("text", text);
  let res = await fetch("http://127.0.0.1:8000/process_text", {method:"POST", body:formData});
  let data = await res.json();
  document.getElementById("output").innerHTML = "<pre>"+JSON.stringify(data,null,2)+"</pre>";
}
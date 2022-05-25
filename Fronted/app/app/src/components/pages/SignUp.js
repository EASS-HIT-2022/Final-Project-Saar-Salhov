import React, { useState } from "react";
import './SignUp.css'


async function createUserAPI(credentials) {
  console.log("before api signup")
  return fetch("http://localhost:4040/users/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(credentials),
  }).then((res) => {
    if (res.ok) {
      console.log("signup succeeded")
      return "success";
    } else {
      if (res.status===401)
      {
        return "Password is too weak or too short";
      }
      else if (res.status===402)
      {
        return "Email is not valid";
      }
      else if(res.status===403)
      {
        return "The username already exists";
      }
      else if (res.status===404)
      {
        return "The password is very common, change it";
      }
    }
  });
}

export default function SignUp() {
      // React States
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [text, setText] = useState();

  var { fname, lname, mail, uname, pass } = document.forms[0];

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("submiting")
        console.log("username", uname)
        console.log("password", pass)
    var cred = {
      firstName: fname,
      lastName:lname,
      email: mail,
      username: uname.toLowerCase(),
      password:pass
    }
    const val = createUserAPI(cred);
    if (val === "success") {
      setIsSubmitted(true);
    } else if (val==="Password is too weak or too short"){
      setText("Password is too weak or too short");
    }else if (val==="Email is not valid"){
      setText("Email is not valid");
    }else if (val==="The username already exists"){
      setText("The username already exists");
    }else if (val==="The password is very common, change it"){
      setText("The password is very common, change it");
    }};
      
    // JSX code for login form
const renderForm = (
  <div className="form">
    <form onSubmit={handleSubmit}>
    <div className="input-container">
        <label>First name </label>
        <input type="text" name="fname" required />
      </div>
      <div className="input-container">
        <label>Last name </label>
        <input type="text" name="lname" required />
      </div>
      <div className="input-container">
        <label>mail </label>
        <input type="text" name="mail" required />
      </div>
      <div className="input-container">
        <label>Username </label>
        <input type="text" name="uname" required />
      </div>
      <div className="input-container">
        <label>Password </label>
        <input type="password" name="pass" required />
        {/* {renderErrorMessage("pass")} */}
      </div>
      <div className="button-container">
        <input type="submit" />
      </div>
    </form>
  </div>
);
  

  return (
    <div className="SignUp">
      <div className="SignUp-form">
        <div className="title">Sign Up</div>
          {isSubmitted ? text : renderForm}
      </div>
    </div>
  )
}

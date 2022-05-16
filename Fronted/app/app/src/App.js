import React from "react";
import NavBar from "./components/NavBar";
import MainContent from "./components/MainContent";
import Footer from "./components/Footer";
import Contact from "./components/Contact";
import image from "./images/user.png"

function App() {
  return (
    <div>
      <NavBar />
      <MainContent />
        <div className="contacts">
          <Contact 
            img = {image}
            name = "Mr. Whiskerson"
            storeName = "Renuar"
            total = "150$"
          />
          <Contact 
            img = {image}
            name = "Mr. Whiskerson"
            storeName = "Renuar"
            total = "150$"
          />
          <Contact 
            img = {image}
            name = "Mr. Whiskerson"
            storeName = "Renuar"
            total = "150$"
          />
        </div>
      <Footer />
    </div>  
  );
}

export default App;

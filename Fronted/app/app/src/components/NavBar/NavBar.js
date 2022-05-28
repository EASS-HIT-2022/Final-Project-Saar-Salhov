import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MenuList from './MenuList';
import Home from '../pages/Home'
import About from '../pages/About'
import Conatct from '../pages/Conatct'
import SignUp from '../pages/SignUp'
import LogIn from '../pages/LogIn'
import NoPage from '../pages/NoPage';


export default function NavBar() {
  const username = localStorage.getItem("username");

  const notLoggedIn = (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<MenuList />}>
        <Route index element={<Home />} />
        <Route path="About" element={<About />} />
        <Route path="Conatct" element={<Conatct />} />
        <Route path="SignUp" element={<SignUp />} />
        <Route path="logIn" element={<LogIn />} />
        </Route>
        <Route path="*" element={<NoPage />} />
    </Routes>
  </BrowserRouter>
  );

  const loggedIn = (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<MenuList />}>
        <Route index element={<Home />} />
        <Route path="About" element={<About />} />
        <Route path="Conatct" element={<Conatct />} />
        <Route path="SignUp" element={<Home />} />
        <Route path="logIn" element={<Home />} />
        </Route>
        <Route path="*" element={<NoPage />} />
    </Routes>
  </BrowserRouter>
  );
  return (
    <div>
      {username? loggedIn : notLoggedIn}
    </div>
  )
}

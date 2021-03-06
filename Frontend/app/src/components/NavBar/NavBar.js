import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MenuList from './MenuList';
import Home from '../pages/Home'
import Receipts from '../pages/Receipts'
import SignUp from '../pages/SignUp'
import LogIn from '../pages/LogIn'
import UploadReceipt from '../pages/UploadReceipt'
import NoPage from '../pages/NoPage';
import ContactUs from '../pages/ContactUs';
import ChangePass from '../pages/ChangePass'


export default function NavBar() {
  const username = localStorage.getItem("username");

  const notLoggedIn = (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<MenuList />}>
        <Route index element={<Home />} />
        <Route path="ContactUs" element={<ContactUs />} />
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
        <Route path="ChangePass" element={<ChangePass />} />
        <Route path="UploadReceipt" element={<UploadReceipt />} />
        <Route path="ContactUs" element={<ContactUs />} />
        <Route path="Receipts" element={<Receipts />} />
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

import React from 'react'
import homeLogo from '../images/logoWithNameNoBG.png'
import './NavBar.css'

export default function NavBar() {
  return (
    <header>
    <nav className="nav">
        <img src={homeLogo} className='nav-logo' alt="" />
        <ul className="nav-items">
            <li>Sign-in</li>
            <li>Sighn-Up</li>
            <li>Contact</li>
        </ul>
    </nav>
    </header>
  )
}

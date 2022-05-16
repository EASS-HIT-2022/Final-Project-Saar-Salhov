import React from 'react'
import './NavBar.css'

export default function NavBar() {
  return (
    <header>
    <nav className="nav">
        <img src="./logoWithName.png" className='nav-logo' alt="" />
        <ul className="nav-items">
            <li>Sign-in</li>
            <li>Sighn-Up</li>
            <li>Contact</li>
        </ul>
    </nav>
    </header>
  )
}

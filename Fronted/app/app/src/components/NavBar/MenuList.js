import { Outlet, Link } from "react-router-dom";
import homeLogo from '../images/logoWithNameNoBG.png'
import './NavBar.css'

const MenuList = () => {
  return (
    <>
      <nav>
      <Link to="/"><img src={homeLogo} className='nav-logo' alt="" /></Link>
        <ul className="nav-items">
          <li>
            <Link to="/About">About</Link>
          </li>
          <li>
            <Link to="/Conatct">Conatct</Link>
          </li>
          <li>
            <Link to="/SignUp">Register</Link>
          </li>
          <li>
            <Link to="/LogIn">Sign-in</Link>
          </li>
          <li>
            <Link to="/">Home</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
  )
};

export default MenuList;
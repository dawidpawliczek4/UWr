import React from "react";
import { Link, NavLink, Outlet } from "react-router-dom";

interface LayoutProps {}

const Layout: React.FC<LayoutProps> = ({}) => {
  return (
    <div className="w-screen bg-slate-900">
      <nav className="flex justify-between px-12 py-6 shadow-white/10 shadow-sm h-[72px]">
        <p>Dawid Pawliczek</p>
        <ul className="flex gap-x-4 font-light h-full">
          <li>
            <NavLink to="/">
              {({ isActive }) => (
                <span className={isActive ? "text-violet-700" : ""}>Home</span>
              )}
            </NavLink>
          </li>
          <li>
            <NavLink to="/about">
              {({ isActive }) => (
                <span className={isActive ? "text-violet-700" : ""}>About me</span>
              )}
            </NavLink>
          </li>
          <li>
            <NavLink to="/projects">
              {({ isActive }) => (
                <span className={isActive ? "text-violet-700" : ""}>Projects</span>
              )}
            </NavLink>
          </li>
          <li>
            <NavLink to="/contact">
              {({ isActive }) => (
                <span className={isActive ? "text-violet-700" : ""}>Contact</span>
              )}
            </NavLink>
          </li>
        </ul>
      </nav>
      <Outlet />
    </div>
  );
};

export default Layout;

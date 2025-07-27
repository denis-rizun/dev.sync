import React, { useEffect, useRef } from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/header.css';

const Header = ({ loginUser }) => {
    const location = useLocation();
    const dropdownRef = useRef(null);

    useEffect(() => {
        if (dropdownRef.current && window.$) {
            window.$(dropdownRef.current).dropdown();
        }
    }, [loginUser]);

    const renderUserActionComp = () => {
        if (loginUser?.id) {
            return (
                <div className="dropdown-wrapper">
                    <span className="username">{loginUser.name}</span>
                    <div className="dropdown-menu">
                        <Link to="/profile" className="dropdown-item">
                            Profile
                        </Link>
                        <a href="/logout" className="dropdown-item">
                            Logout
                        </a>
                    </div>
                </div>
            );
        }
        return (
            <a href="/login" className="login-link">
                Login
            </a>
        );
    };

    const navItems = [
        { path: '/webhook', label: 'Webhooks' },
        { path: '/server', label: 'Servers' },
        { path: '/doc', label: 'Documents' },
    ];

    return (
        <header className="custom-header">
            <div className="left-section">
                <Link to="/" className="logo-link">
                    <img
                        src="../assets/favicon.png"
                        alt="Logo"
                        width="40"
                        height="40"
                    />
                </Link>
                {navItems.map((item) => (
                    <Link
                        key={item.path}
                        to={item.path}
                        className={`nav-link ${location.pathname.startsWith(item.path) ? 'active' : ''}`}
                    >
                        {item.label}
                    </Link>
                ))}
            </div>
            <div className="right-section">
                {loginUser?.avatar && (
                    <img
                        className="avatar"
                        width="32"
                        height="32"
                        src={loginUser.avatar}
                        alt="User Avatar"
                    />
                )}
                {renderUserActionComp()}
            </div>
        </header>
    );
};

export default Header;

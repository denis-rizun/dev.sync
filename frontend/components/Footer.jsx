import React from 'react';
import '../styles/footer.css';

const Footer = () => {
    return (
        <footer className="custom-footer">
            <div>
                &copy; 2025 |
                <a href="https://github.com/denis-rizun" target="_blank">
                    {' '}
                    Denis Rizun{' '}
                </a>
                | All rights reserved.
            </div>
        </footer>
    );
};

export default Footer;

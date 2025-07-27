import React, { useState, useEffect } from "react";
import AuthContext from "./AuthContext";
import {getProfile, refreshAccessToken} from "./authService";

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const initializeAuth = async () => {
            const storedProfile = localStorage.getItem("user_profile");
            const storedAccessToken = localStorage.getItem("access_token");

            if (!storedAccessToken) {
                return;
            }
            if (storedProfile) {
                setUser(JSON.parse(storedProfile));
                return;
            }

            try {
                let profile;
                try {
                    profile = await getProfile();
                } catch (err) {
                    const { accessToken } = await refreshAccessToken();
                    localStorage.setItem("access_token", accessToken);
                    profile = await getProfile();
                }
                localStorage.setItem("user_profile", JSON.stringify(profile));
                setUser(profile);
            } catch (err) {
                console.error("Ошибка при инициализации авторизации:", err);
                setUser(null);
            }
        };


        initializeAuth();
    }, []);


    return (
        <AuthContext.Provider value={{ user, setUser }}>
            {children}
        </AuthContext.Provider>
    );
}

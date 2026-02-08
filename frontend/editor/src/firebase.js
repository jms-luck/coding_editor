import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyCh_FuaaqVgX01smPNV_Lj_zn5kzwZXCMg",
  authDomain: "ditor-e2486.firebaseapp.com",
  projectId: "ditor-e2486",
  storageBucket: "ditor-e2486.firebasestorage.app",
  messagingSenderId: "129270848040",
  appId: "1:129270848040:web:1e416bd13029f0626fb31d",
  measurementId: "G-24GYPWFSY6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Analytics
const analytics = getAnalytics(app);

// Initialize Authentication
export const auth = getAuth(app);

export default app;

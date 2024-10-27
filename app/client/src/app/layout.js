'use client'

import localFont from "next/font/local";
import "./globals.css";
import * as React from 'react';
import { createTheme, styled } from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import TimelineIcon from '@mui/icons-material/Timeline';
import { AppProvider } from '@toolpad/core/nextjs'; // Next.js
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import StadiumIcon from '@mui/icons-material/Stadium';
import GroupsIcon from '@mui/icons-material/Groups';
import SportsSoccerIcon from '@mui/icons-material/SportsSoccer';
import PersonIcon from '@mui/icons-material/Person';

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

const NAVIGATION = [
  {
    kind: 'header',
    title: 'Menu',
  },
  {
    segment: 'players',
    title: 'Jogadores',
    icon: <PersonIcon />
  },
  {
    segment: 'teams',
    title: 'Times',
    icon: <GroupsIcon />
  },
  {
    segment: 'games',
    title: 'Jogos',
    icon: <SportsSoccerIcon />
  },
  {
    segment: 'stadiums',
    title: 'Estádios',
    icon: <StadiumIcon />,
  },
];

const theme = createTheme({
  cssVariables: {
    colorSchemeSelector: 'data-toolpad-color-scheme',
  },
  colorSchemes: { 
    light: {
      palette: {
        primary: {
            main: '#000',
        },
        secondary: {
            main: '#dc004e',
        },
      }
    }, 
    dark: {
      palette: {
        primary: {
            main: '#fff',
        },
        secondary: {
            main: '#dc004e',
        },
      }
    },
  },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  }
});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
            <AppProvider
              navigation={NAVIGATION}
              theme={theme}
              branding={{
                logo: <img src="https://static.vecteezy.com/system/resources/previews/015/863/623/non_2x/england-premier-league-logo-on-transparent-background-free-vector.jpg" alt="Football" />,
                title: '2022 Premier League Dashboard',
              }}
            >
              <DashboardLayout defaultSidebarCollapsed>
                {children}
              </DashboardLayout>
            </AppProvider>
      </body>
    </html>
  );
}

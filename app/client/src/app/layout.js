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
    segment: 'stadiums',
    title: 'Estádios',
    icon: <StadiumIcon />,
  },
  {
    segment: 'page-2',
    title: 'Page 2',
    icon: <TimelineIcon />,
  },
];

const theme = createTheme({
  cssVariables: {
    colorSchemeSelector: 'data-toolpad-color-scheme',
  },
  colorSchemes: { light: true, dark: true },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 600,
      lg: 1200,
      xl: 1536,
    },
  },
});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
            <AppProvider
              navigation={NAVIGATION}
              theme={theme}
              branding={{
                logo: <img src="https://www.svgrepo.com/show/17072/football.svg" alt="Football" />,
                title: 'Dashboard',
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

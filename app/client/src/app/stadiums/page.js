'use client'

import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { createTheme, styled } from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import TimelineIcon from '@mui/icons-material/Timeline';
import { AppProvider } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { useDemoRouter } from '@toolpad/core/internal';
import { PageContainer, PageContainerToolbar } from '@toolpad/core/PageContainer';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import CardsSection from '../components/cardsSection'

function Stadiums() {
  return (
    <Paper sx={{ borderRadius: '0', p: 2, width: '100%', height: '100vh' }}>
      <PageContainer maxWidth="lg">
        <CardsSection title={'Os 3 estádios com maiores capacidades'} />
        <CardsSection title={'Os 3 estádios com menores capacidades'} />
      </PageContainer>
    </Paper>
  );
}

export default Stadiums;

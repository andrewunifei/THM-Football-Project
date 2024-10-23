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
import Divider from '@mui/material/Divider';
import MediaCard from '../components/mediaCard';
import { borderColor } from '@mui/system';


function Stadiums() {
  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="lg">
        <Grid container spacing={3} >
          <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
              <Box>
                <MediaCard/>
              </Box>
            </Paper>
          </Grid>
          <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
              <Box>
                <MediaCard/>
              </Box>
            </Paper>
          </Grid>
        </Grid>
        <div style={{paddingTop:'30px'}}></div>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          <CardsSection title={'Estádios com maiores capacidades'} />
        </Paper>
        <div style={{paddingTop:'30px'}}></div>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          <CardsSection title={'Estádios com menores capacidades'} />
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Stadiums;

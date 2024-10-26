'use client'

import { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import CardsSection from '../components/stadiums/cardsSection'
import { getTopStadiums, getBottomStadiums } from '../api/stadium';
import StadiumsBarChart from '../components/stadiums/stadiumsBarChart';
import PieChart from '../components/stadiums/stadiumPieChart';

function Stadiums() {
  const [topStadiumsInfo, setTopStadiumsInfo] = useState({});
  const [bottomStadiumsInfo, setBottomStadiumsInfo] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const dataTopStadiums = await getTopStadiums()
      setTopStadiumsInfo(dataTopStadiums)
      const dataBottomStadiums = await getBottomStadiums()
      setBottomStadiumsInfo(dataBottomStadiums)
    }
    fetchData()
  }, []);

  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="xl">
        <Grid container spacing={3} >
          <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
              <Box sx={{height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <StadiumsBarChart/>
              </Box>
            </Paper>
          </Grid>
          <Grid size={6} sx={{border: '2px', borderColor: '#fff'}}>
            <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
              <Box sx={{height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <PieChart/>
              </Box>
            </Paper>
          </Grid>
        </Grid>
        <div style={{paddingTop:'25px'}}></div>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          <CardsSection title={'Maiores Estádios'} media={topStadiumsInfo ? topStadiumsInfo : ''} />
        </Paper>
        <div style={{paddingTop:'25px'}}></div>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          <CardsSection title={'Menores Estádios'} media={bottomStadiumsInfo ? bottomStadiumsInfo: ''}/>
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Stadiums;

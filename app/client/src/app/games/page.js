'use client'

import { useEffect, useState, Fragment } from 'react';
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';
import Grid from '@mui/material/Grid2';
import { getGamesCategorized } from '../api/game';
import GamesTable from '../components/games/gamesTables';

const months = [
  "Janeiro",
  "Fevereiro",
  "Março",
  "Abril",
  "Maio",
  "Junho",
  "Julho",
  "Agosto",
  "Setembro",
  "Outubro",
  "Novembro",
  "Dezembro"
]

function mountTable(gamesCategorized, year) {
  return(
    [...months].reverse().map((item, index) => (
      <>
        {(gamesCategorized[0][year][item]?.length > 0 && gamesCategorized[0][year][item][0]['date']?.slice(12, 16) == String(year)) ? 
        (<>
          <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>{(gamesCategorized[0][year][item].length > 0) ? (`${[...months].reverse()[index]} ${gamesCategorized[0][year][item][0]['date'].slice(12, 16)}`) : ''}</p>
          <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
          <Grid container sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
              <Grid size={12} >
                  <Box style={{marginBottom: '40px'}}>
                    <GamesTable games={gamesCategorized[0][year][item]} />
                  </Box>
              </Grid>
            </Grid>
          </>) : ''}
        </>
      )
    )
  )
}

function Games() {
  const [gamesCategorized, setGamesCategorized] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const data = await getGamesCategorized()
      setGamesCategorized([data])
    }
    fetchData()
  }, []);

  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="xl" sx={{marginBottom: '150px'}}>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          {gamesCategorized[0] ? [...Object.keys(gamesCategorized[0])].reverse().map((item, index) => (
            mountTable(gamesCategorized, String(item))
          )): ''}
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Games;

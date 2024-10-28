'use client'

import { useEffect, useState, Fragment } from 'react';
import Box from '@mui/material/Box';
import Link from 'next/link';
import { PageContainer } from '@toolpad/core/PageContainer';
import Paper from '@mui/material/Paper';
import { getPlayersCategorized } from '../api/player';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListItemText from '@mui/material/ListItemText';
import ListItemButton from '@mui/material/ListItemButton';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import Grid from '@mui/material/Grid2';
import { getGamesCategorized } from '../api/game';

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
        {gamesCategorized[0] ? months.map((item, index) => (
          <>
            {(gamesCategorized[0][item].length > 0) ? 
            (<>
              <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>{(gamesCategorized[0][item].length > 0) ? months[index] : ''}</p>
              <Divider orientation="horizontal" style={{marginBottom: '40px'}} />
              <Grid container sx={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                  <Grid size={12} >
                      <Box>
                          {
                            gamesCategorized[0][item].map((item, index) => {
                              return (<>
                                <p>{item['date']}</p>
                              </>)
                            })     
                            // gamesCategorized[0][item].forEach((element) => {
                            //   console.log(element['date'])
                            // })                       
                          }
                      </Box>
                  </Grid>
              </Grid>
            </>) : ''}
          </>
        )) : ''}
      </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Games;

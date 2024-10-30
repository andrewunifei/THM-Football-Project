'use client'

import { useEffect, useState, useRef } from 'react';
import Box from '@mui/material/Box';
import { PageContainer } from '@toolpad/core/PageContainer';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';
import Grid from '@mui/material/Grid2';
import { getGamesCategorized, getGamesAvailable } from '../api/game';
import GamesTable from '../components/games/gamesTables';
import { getTeamsMatch } from '../api/team';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import Button from '@mui/material/Button';

const months_mapping = {
  1: "Janeiro",
  2: "Fevereiro",
  3: "Março",
  4: "Abril",
  5: "Maio",
  6: "Junho",
  7: "Julho",
  8: "Agosto",
  9: "Setembro",
  10: "Outubro",
  11: "Novembro",
  12: "Dezembro"
}

function Games() {
  const [gamesAvailable, setGamesAvailable] = useState({});
  const [games, setGames] = useState()
  const [currentmonth, setCurrentMonth] = useState('')

  async function handleAccordion(year, month) {
    if(!games || currentmonth != month){
      const games_data = await getGamesCategorized(year, month)
      setGames(games_data)
    }
    setCurrentMonth(month)
  }
  
  function mountAccordion(gamesCategorized, year) {
    return(
      [...gamesCategorized[0][year]].reverse().map((month, index) => (
          <>
            <Grid container sx={{display: 'flex', alignmonths: 'center', justifyContent: 'center'}}>
                <Grid size={12} >
                  <Accordion id={month} onChange={()=>{handleAccordion(year, month)}}>
                    <AccordionSummary
                      expandIcon={<ArrowDownwardIcon />}
                      aria-controls="panel1-content"
                      id="panel1-header"
                    >
                      <span style={{fontSize: '20px', font: 'roboto', fontWeight: '100'}}>
                        {months_mapping[month]}
                      </span>
                    </AccordionSummary>
                      <AccordionDetails>
                        {games?(<GamesTable games={games}/>):''}
                      </AccordionDetails>
                  </Accordion>
                </Grid>
              </Grid>
          </>
        )
      )
    )
  }

  useEffect(() => {
    const fetchData = async () => {
      const data = await getGamesAvailable()
      setGamesAvailable([data])
    }
    fetchData()
  }, []);

  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="xl" sx={{marginBottom: '150px'}}>
        <Paper sx={{borderRadius: 3, p: 5}} elevation={3}>
          {gamesAvailable[0] ? [...Object.keys(gamesAvailable[0])].reverse().map((item, index) => (
            <Box sx={{marginBottom: '45px'}}>
              <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>{item}</p>
              <Divider orientation="horizontal" style={{marginBottom: '20px'}} />
              {mountAccordion(gamesAvailable, String(item))}
            </Box>
          )): ''}
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Games;

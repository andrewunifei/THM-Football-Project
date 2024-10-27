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

function getTitle(logo, name) {
  return (
      <List sx={{ width: '100%', display: 'flex', alignItems:"flex-start"}} >
          <ListItem>
              <ListItemAvatar>
                  <Avatar alt="logo" src={logo}/>
              </ListItemAvatar>
              <p style={{fontSize: '24px', font: 'roboto', fontWeight: '100'}}>{name}</p>
          </ListItem>
      </List>
  )
}

function getParams(player) {
  return `players/explore?player-id=${player?.player_id}&photo=${player?.photo}&name=${player?.name}`
}

function Players() {

  const [playersCategorized, setPlayersCategorized] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getPlayersCategorized()
      setPlayersCategorized(data)
    }
    fetchData()
  }, []);

  return (
    <Paper sx={{borderRadius: 0, p: 2, width: '100%', height: '100vh', overflow: 'auto' }} elevation={1}>
      <PageContainer maxWidth="xl" sx={{marginBottom: '150px'}}>
        {playersCategorized ? playersCategorized.map((item, index) => (
          <>
            <Paper sx={{borderRadius: 3, p: 3}} elevation={3}>
                <Accordion>
                <AccordionSummary
                  expandIcon={<ArrowDownwardIcon />}
                  aria-controls="panel1-content"
                  id="panel1-header"
                >
                  {getTitle(playersCategorized[index]?.logo, playersCategorized[index]?.team)}
                </AccordionSummary>
                <AccordionDetails>
                  <List sx={{ width: '100%', overflow: 'auto' }}>
                    {playersCategorized ? playersCategorized[index]['players'].map((player, index2) => (
                      <Box>
                        <ListItemButton key={index2} alignItems="flex-start" component={Link} to={getParams(player, index)}>
                            <ListItemAvatar>
                                <Avatar alt="logo" src={player.photo} />
                            </ListItemAvatar>
                            <ListItemText
                                primary={player.name}
                                secondary={
                                    <Fragment>
                                    <Typography
                                        component="span"
                                        variant="body2"
                                        sx={{ color: 'text.secondary', display: 'block' }}
                                    >
                                        <span style={{fontWeight:'bold'}}>Posição:</span> {player.position}
                                    </Typography>
                                    <Typography
                                        component="span"
                                        variant="body2"
                                        sx={{ color: 'text.secondary', display: 'block' }}
                                    >
                                        <span style={{fontWeight:'bold'}}>Idade:</span> {player.age}
                                    </Typography>
                                    <Typography
                                        component="span"
                                        variant="body2"
                                        sx={{ color: 'text.secondary', display: 'block' }}
                                    >
                                        <span style={{fontWeight:'bold'}}>Nacionalidade:</span> {player.nationality}
                                    </Typography>                                            
                                    <Typography
                                        component="span"
                                        variant="body2"
                                        sx={{ color: 'text.secondary', display: 'block' }}
                                    >
                                        <span style={{fontWeight:'bold'}}>Machucado?</span>
                                        {player.injured ? <span style={{color: 'red'}}> Sim</span> : <span style={{color: 'green'}}> Não</span>}
                                    </Typography>   
                                    </Fragment>
                                }
                            />
                        </ListItemButton>
                        <Divider variant="inset" component="li" />
                      </Box>
                  )) : ''}
                  </List>
                </AccordionDetails>
              </Accordion>
            </Paper>
            <div style={{paddingTop:'25px'}}></div>
          </>
        )) : ''}
      </PageContainer>
    </Paper>
  );
}

export default Players;

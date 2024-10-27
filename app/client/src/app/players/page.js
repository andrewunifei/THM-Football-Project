'use client'

import { useEffect, useState } from 'react';
import { PageContainer } from '@toolpad/core/PageContainer';
import Paper from '@mui/material/Paper';
import { getPlayersCategorized } from '../api/player';
import Avatar from '@mui/material/Avatar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';

function getTitle(logo, name) {
  return (
      <List sx={{ width: '100%', display: 'flex', alignItems:"flex-start"}} >
          <ListItem>
              <ListItemAvatar>
                  <Avatar alt="logo" src={logo}/>
              </ListItemAvatar>
              <p style={{fontSize: '34px', font: 'roboto', fontWeight: '100'}}>{name}</p>
          </ListItem>
      </List>
  )
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
        <Paper sx={{borderRadius: 3, p: 3}} elevation={3}>
          {getTitle(playersCategorized?.Arsenal?.logo, 'Arsenal')}
        </Paper>
      </PageContainer>
    </Paper>
  );
}

export default Players;

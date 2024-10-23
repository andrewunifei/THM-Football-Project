import * as React from 'react';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import MediaCard from './mediaCard';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';

export default function CardsSection({ title }) {
    return (
        <Box style={{paddingBottom: '10px', paddingTop: '10px'}}>
            <p style={{paddingBottom: '10px', font: 'roboto'}}>{title}</p>
            <Divider orientation="horizontal" style={{marginBottom: '15px'}} />
            <Grid container spacing={1} >
                <Grid size={4}>
                    <Box>
                        <MediaCard/>
                    </Box>
                </Grid>
                <Grid size={4}>
                    <Box>
                        <MediaCard/>
                    </Box>
                </Grid>
                <Grid size={4}>
                    <Box>
                        <MediaCard/>
                    </Box>
                </Grid>
            </Grid>
        </Box>
    )
}
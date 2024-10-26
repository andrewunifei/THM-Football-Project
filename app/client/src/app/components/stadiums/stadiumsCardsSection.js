import * as React from 'react';
import Grid from '@mui/material/Grid2';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import StadiumsMediaCard from './stadiumsMediaCard';

export default function StadiumsCardsSection({ title, media=false }) {
    return (
        <Box style={{paddingBottom: '10px', paddingTop: '10px'}}>
            <p style={{paddingBottom: '10px', font: 'roboto'}}>{title}</p>
            <Divider orientation="horizontal" style={{marginBottom: '15px'}} />
            <Grid container spacing={1} >
                <Grid size={4}>
                    <Box>
                        <StadiumsMediaCard media={media ? media[0] : ''} />
                    </Box>
                </Grid>
                <Grid size={4}>
                    <Box>
                        <StadiumsMediaCard media={media ? media[1] : ''} />
                    </Box>
                </Grid>
                <Grid size={4}>
                    <Box>
                        <StadiumsMediaCard media={media ? media[2] : ''} />
                    </Box>
                </Grid>
            </Grid>
        </Box>
    )
}
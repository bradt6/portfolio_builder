import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

import Services from '../Services/Services';
import Portfolio from '../Portfolio/Portfolio';
import Home from '../Home/Home';

function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box p={3}>
                    <Typography>{children}</Typography>
                </Box>
            )}
        </div>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
};

function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        'aria-controls': `simple-tabpanel-${index}`,
    };
}

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        backgroundColor: 'theme.palette.background.paper',
    },
    navColor: {
        backgroundColor: 'black',
    },
}));

export default function NavBar() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return (
        <div className={classes.root}>
            <AppBar className={classes.navColor} position="static">
                <Tabs value={value} onChange={handleChange} aria-label="simple tabs example">
                    <Tab label="Home" {...a11yProps(0)} />
                    <Tab label="Services" {...a11yProps(1)} />
                    <Tab label="Contact" {...a11yProps(2)} />
                    <Tab label="Portfolio" {...a11yProps(3)} />
                    <Tab label="About" {...a11yProps(4)} />
                </Tabs>
            </AppBar>
            <TabPanel value={value} index={0}>
                <Home></Home>
            </TabPanel>
            <TabPanel value={value} index={1}>
                <Services></Services>
            </TabPanel>
            <TabPanel value={value} index={2}>
                Contact
            </TabPanel>
            <TabPanel value={value} index={3}>
                <Portfolio></Portfolio>
            </TabPanel>
            <TabPanel value={value} index={4}>
                About
            </TabPanel>
      
        </div>
    );
}

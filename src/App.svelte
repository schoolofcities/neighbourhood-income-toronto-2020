<script>

	import Top from "./lib/TopSofC.svelte";
	import UnderConstruction from "./lib/UnderConstruction.svelte";
	import MapTop from "./lib/MapTop.svelte";
	import MapDiff from "./lib/MapDiff.svelte";
	import MapMini from "./lib/MapMini.svelte";
	import BigNumber from "./lib/BigNumber.svelte";
	import Legend from "./lib/Legend.svelte";
	import LegendDiff from "./lib/LegendDiff.svelte";
	import inc1960 from "./data/1960.geo.json";
	import inc1970 from "./data/1970.geo.json";
	import inc1980 from "./data/1980.geo.json";
	import inc1990 from "./data/1990.geo.json"
	import inc2000 from "./data/2000.geo.json";
	import inc2010 from "./data/2010.geo.json";
	import inc2020 from "./data/2020.geo.json";

	let coloursDiv = ["#DC4633", "#ee9d78", "#f2dfce", "#7eb4b3", "#007fa3"];
	let coloursDiv2 = ["#316961", "#9dab9e", "#f2dfce", "#ad7ea2", "#824287"].reverse();
	let coloursSeqRed = ['#f2dfce','#ecb4a2','#e5816f','#dc4633','#ed1b00'];
	let coloursSeqBlue = ['#f2dfce','#b3c6c3','#79afb9','#3d97ae','#007fa3'];
	let spacing = [50, 100, 150, 200, 250]

	const avg_hhld_inc_2020 = 110000;
	const avg_ind_inc_2020 = 60000;
	const pov_lim_2020 = 18.2;
	const med_hhld_inc_2020 = 90000;
	const med_ind_inc_2020 = 42000;
	const pop_den_2020 = 4200;

	$: currentLayer = "hhld_inc";
	$: currentLayerDiff = "hhld_inc";
	
</script>

<svelte:head>
	<link
		href="https://fonts.googleapis.com/css2?family=Bitter&family=Playfair+Display&display=swap"
		rel="stylesheet"
	/>
	<link
		href="https://fonts.googleapis.com/css2?family=Roboto&family=Source+Serif+Pro&display=swap"
		rel="stylesheet"
	/>
	<meta
		name="viewport"
		content="width=device-width, initial-scale=1, minimum-scale=1"
	/>
</svelte:head>




<Top/>

<main>

	<UnderConstruction/>

	<div class="title">

		<div id="mini-line"></div>

		<h1>Wealth inequalities and poverty concentration in Toronto</h1>

		<div class="circles">
			<svg>
			  {#each [0,1,2,3,4] as d}
				<circle cx={spacing[d]} cy="10px" r=10 fill={coloursDiv[d]} stroke= "white" stroke-width="2px" />
			  {/each}
			</svg>
		</div>
		
		<h3>A first look at 2020 annual income data collected as part of the 2021 census</h3>
		<br>

		<div id="mini-line"></div>

	</div>

	


	<div class="text">
		<p>On July 13, 2022, Statistics Canada released data on individual and household yearly income for 2020. Using this data, we are able to create neighbourhood-level maps of the City of Toronto showing where wealth and poverty are concentrated. These highlight ... ... ...</p>
	</div>

	<div id="top-map">
		<div class="layer-button-wrapper">
			<button 
			class:selected="{currentLayer === 'pov_lim'}"
			class:not-selected="{currentLayer !== 'pov_lim'}"
			on:click="{() => currentLayer = 'pov_lim'}"  id="pov_lim">Poverty Rate</button>
	
			<button 
			class:selected="{currentLayer === 'hhld_inc_m'}"
			class:not-selected="{currentLayer !== 'hhld_inc_m'}"
			on:click="{() => currentLayer = 'hhld_inc_m'}"
			id="hhld_inc_m">Median Household Income</button>
	
			<button 
			class:selected="{currentLayer === 'hhld_inc'}"
			class:not-selected="{currentLayer !== 'hhld_inc'}"
			on:click="{() => currentLayer = 'hhld_inc'}"
			id="hhld_inc">Average Household Income</button>
	
			<button 
			class:selected="{currentLayer === 'ind_inc_m'}"
			class:not-selected="{currentLayer !== 'ind_inc_m'}"
			on:click="{() => currentLayer = 'ind_inc_m'}" id="ind_inc_m">Median Individual Income</button>
		
			<button 
			class:selected="{currentLayer === 'ind_inc'}"
			class:not-selected="{currentLayer !== 'ind_inc'}"
			on:click="{() => currentLayer = 'ind_inc'}" id="ind_inc">Average Individual Income</button>
	
			<button 
			class:selected="{currentLayer === 'pop_den'}"
			class:not-selected="{currentLayer !== 'pop_den'}"
			on:click="{() => currentLayer = 'pop_den'}"  id="pop_den">Population Density</button>
		</div>
		
		<div class="mapBig">
			<MapTop coloursD = {coloursDiv} coloursSR = {coloursSeqRed} coloursSB = {coloursSeqBlue} currentLayer={currentLayer}/>
		</div>
	</div>

	<div class="top-info">
		<div class="legend">
			<Legend 
				layer = {currentLayer}
				coloursDiv = {coloursDiv}
				coloursSeqRed = {coloursSeqRed} coloursSeqBlue = {coloursSeqBlue}
			/>
		</div>
		<div class="big-number-box">
			<BigNumber type = {"pov_lim" === currentLayer} number={pov_lim_2020 + "%"} label={"Poverty Rate (LIM)"}/>
			<BigNumber type = {"hhld_inc_m" === currentLayer} number={"$" + med_hhld_inc_2020.toLocaleString("en-US")} label={"Median Household Income"}/>
			<BigNumber type = {"hhld_inc" === currentLayer} number={"$" + avg_hhld_inc_2020.toLocaleString("en-US")} label={"Average Household Income"}/>
			<BigNumber type = {"ind_inc_m" === currentLayer} number={"$" + med_ind_inc_2020.toLocaleString("en-US")} label={"Median Individual Income"}/>
			<BigNumber type = {"ind_inc" === currentLayer} number={"$" + avg_ind_inc_2020.toLocaleString("en-US")} label={"Average Individual Income"}/>
			<BigNumber type = {"pop_den" === currentLayer} number={pop_den_2020.toLocaleString("en-US")} label={"Population Density (p/km2)"}/>
		</div>
	</div>






	
	<div id="mini-line"></div>

	<div class="text">
		<p>Now let's take a look at how these patterns have changed over time. The following map shows the percent difference in neighbourhood income between 2020 and 2015 (accounting for inflation). The green areas indicate an increase and the purple areas indicate a decrease. These show that ... ... ...</p>
	</div>

	<LegendDiff coloursDiv={coloursDiv2}/>

	<div class="layer-button-wrapper">
		<button 
		class:selected="{currentLayerDiff === 'pov_lim'}"
		class:not-selected="{currentLayerDiff !== 'pov_lim'}"
		on:click="{() => currentLayerDiff = 'pov_lim'}"  id="pov_lim">Poverty Rate</button>

		<button 
		class:selected="{currentLayerDiff === 'hhld_inc_m'}"
		class:not-selected="{currentLayerDiff !== 'hhld_inc_m'}"
		on:click="{() => currentLayerDiff = 'hhld_inc_m'}"
		id="hhld_inc_m">Median Household Income</button>

		<button 
		class:selected="{currentLayerDiff === 'hhld_inc'}"
		class:not-selected="{currentLayerDiff !== 'hhld_inc'}"
		on:click="{() => currentLayerDiff = 'hhld_inc'}"
		id="hhld_inc">Average Household Income</button>

		<button 
		class:selected="{currentLayerDiff === 'ind_inc_m'}"
		class:not-selected="{currentLayerDiff !== 'ind_inc_m'}"
		on:click="{() => currentLayerDiff = 'ind_inc_m'}" id="ind_inc_m">Median Individual Income</button>
	
		<button 
		class:selected="{currentLayerDiff === 'ind_inc'}"
		class:not-selected="{currentLayerDiff !== 'ind_inc'}"
		on:click="{() => currentLayerDiff = 'ind_inc'}" id="ind_inc">Average Individual Income</button>

		<button 
		class:selected="{currentLayerDiff === 'pop_den'}"
		class:not-selected="{currentLayerDiff !== 'pop_den'}"
		on:click="{() => currentLayerDiff = 'pop_den'}"  id="pop_den">Population Density</button>
	</div>

	<div class="mapBig">
		<MapDiff coloursD = {coloursDiv2} currentLayer={currentLayerDiff}/>
	</div>




	<div class="text"> </div>

	<div id="mini-line"></div>

	<div class="text">
		<p>Over a longer term, the spatial patterns of wealth and poverty in the city have changed substantially. Below are a series of maps showing <span id="bold">average household income</span> for each of the six decades prior to 2020. These clearly show that lower-income residents were once clustered in the centre, in and around downtown Toronto, but have since additionally concentrated in more suburban neighbourhoods, particularly in the northeast and northwest of the city, a trend often cited as a suburbanization of poverty.
	</div>

	<div class="mapGrid">
		<div class="mapSmall">
			<MapMini year={"1960"} tracts={inc1960.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div>
		<div class="mapSmall">
			<MapMini year={"1970"} tracts={inc1970.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div>
		<div class="mapSmall">
			<MapMini year={"1980"} tracts={inc1980.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div><div class="mapSmall">
			<MapMini year={"1990"} tracts={inc1990.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div>
		<div class="mapSmall">
			<MapMini year={"2000"} tracts={inc2000.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div>
		<div class="mapSmall">
			<MapMini year={"2010"} tracts={inc2010.features} colours = {coloursDiv}  variable={"avg_inc"}/>
		</div>
		<div class="mapSmall">
			<MapMini year={"2020"} tracts={inc2020.features} colours = {coloursDiv}  variable={"ah16"}/>
		</div>
		<div class="legend">
			<Legend 
				layer = {"hhld_inc"}
				coloursDiv = {coloursDiv}
				coloursSeqRed = {coloursSeqRed} coloursSeqBlue = {coloursSeqBlue}
			/>
		</div>
	</div>

	<div id="mini-line"></div>

	<div class="text">
		<p>This is just a first look at this data, certainly more research and context is needed to further understand the how and why of these patterns and their changes over time.</p>
	</div>	



	<div id="mini-line"></div>

	<div class="info">
		<h3>Data Sources & More Information</h3>
		<p>
		This page and its content were compiled by <a href="https://jamaps.github.io">Jeff Allen</a> at the <a href="https://www.schoolofcities.utoronto.ca/">School of Cities</a>.
		</p>
			
		<p>
		The 2021 census data were accessed from <a href="https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E">Statistics Canada</a> while the historical data were accessed via <a href="http://chass.toronto.edu/">CHASS</a> and the <a href="https://mdl.library.utoronto.ca/">Map and Data Library</a> at the University of Toronto. The spatial units on the maps are neighbourhood-sized census tracts, which approximately correspond to approximately 2,500 and 8,000 residents. Data on the povert rate is based on the after-tax <a href="https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/Definition-eng.cfm?ID=fam021">Low-Income Measure</a>, a poverty line defined by Statistics Canada. The map comparing 2015 to 2020 data makes use of the <a href="https://github.com/jamaps/CLTD">Canadian Longitudinal Tract Database</a> to apportion data to the same spatial units.
		</p>

		<p>
		For the maps from 1960 to 2010, only average household income is shown due to a lack of data from historical censuses. For 1960 specifically, due to lack of data, the variable mapped is average family income rather than average household income. <a href="https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/Definition-eng.cfm?ID=fam004">Census families</a> are a subset of all <a href="https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/Definition-eng.cfm?ID=households-menage007">households</a> so even though the patterns are likely quite similar, this should be treated with caution since it does not allow for a direct comparison with later years. 
		</p>
		
		<p>
		The maps were created using <a href="https://d3js.org/">D3</a> and <a href="https://svelte.dev/">Svelte</a>. Code and data for this page are hosted on <a href="https://github.com/schoolofcities/neighbourhood-income-toronto-2021">GitHub</a>. 
		</p>

		<p>
		For more information on the changing patterns of income in Toronto and other Canadian cities, check out resources from the <a href="http://neighbourhoodchange.ca/cities/toronto/">Neighbourhood Change Research Partnership</a>
		</p>
	</div>


</main>


<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #fff9f4;
	}

	main {
		margin: 0 auto;
		width: 100%;
		min-width: 320px;
		max-width: 1200px;
		position: relative;
	}

	.circles {
		margin: auto;
		max-width: 300px;
		margin-top: 10px;
		height: 25px;
	}

	.title {
		margin: auto;
		max-width: 600px;
		width: calc(100% - 50px);
		padding-left: 25px;
		padding-right: 25px;
		margin-top: 100px;
		text-align: center;
		font-family: "Source Serif Pro", serif;
	}
	.title h1 {
		font-weight: normal;
		font-size: 40px;
	}
	.title h3 {
		font-weight: normal;
		font-size: 18px;
	}

	#mini-line {
		margin: auto;
		width: 220px;
		height: 1px;
		background-color: black;
	}

	.text {
		font-family: "Source Serif Pro", serif;
		font-size: 16px;
		margin: auto;
		max-width: 594px;
		width: calc(100% - 50px);
		padding: 25px;
		line-height: 160%;
		text-align: left;
	}
	a {
		text-decoration: none;
		color: #007fa3;
	}

	.layer-button-wrapper {
		margin: auto;
		max-width: 600px;
		width: 100%;
		min-width: 375px;
	}
	@media (max-width:620px) {
		.layer-button-wrapper {
			padding-left: 25px;
			width: calc(100% - 25px);
		}
	}
	.layer-button-wrapper button {
		border: solid 1px rgb(176, 176, 176);
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		cursor: pointer;
		border-radius: 1px;
		padding: 4px;
		margin-top: 4px;
		/* background-color: #f2dfce; */
	}
	.selected {
		background-color: #ffffff;
		color: rgb(22, 22, 22);;
	}
	.not-selected {
		background-color: #f2dfce;
		color: rgb(103, 103, 103);
	}
	.layer-button-wrapper button:hover {
		color: #007fa3;
	}

	.mapBig {
		margin: auto;
		max-width: 810px;
		border: solid 1px rgb(238, 238, 238);
		border-radius: 5px; 
		border-bottom-right-radius: 200px;
	}

	@media (max-width:420px) {
		.mapBig {
			border: none;
		}
	}

	.top-info {
		margin: auto;
		width: 580px;
		overflow: hidden;
		display: grid;
		gap: 0px 0px;
		grid-template-columns: repeat(2, 1fr);
		padding-bottom: 25px;
	}

	@media (max-width:580px) {
		.top-info {
			grid-template-columns: repeat(1, 1fr);
			width: 300px;
		}
	}

	.big-number-box {
		margin: auto;
		margin-top: 0px;
		width: 280px;
	}
	.legend {
		margin: auto;
		max-width: 300px;
	}

	#bold {
		color: #ed1b00;
		font-weight: bold;	
	}

	.mapGrid {
		margin: auto;
		padding-bottom: 42px;
		max-width: 820px;
		width: 100%;
		display: grid;
		gap: 10px 10px;
		grid-template-columns: repeat(2, 1fr);
	}

	@media (max-width:820px) {
		.mapGrid {
			grid-template-columns: repeat(1, 1fr);
			/* gap: 0px 0px; */
			width: calc(100% - 40px);
		}
	}

	.mapSmall {
		margin: auto;
		padding: -10px;
		max-width: 400px;
		border: solid 1px rgb(238, 238, 238);
		border-radius: 10px;
		border-bottom-right-radius: 100px;
	}

	.info {
		font-family: "Source Serif Pro", serif;
		font-size: 14px;
		margin: auto;
		max-width: 494px;
		width: calc(100% - 50px);
		padding: 25px;
		line-height: 160%;
		text-align: left;
	}
	
</style>

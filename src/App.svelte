<script>

	import Top from "./lib/TopSofC.svelte";
	import MapTop from "./lib/MapTop.svelte";
	import MapMini from "./lib/MapMini.svelte";
	import Legend from "./lib/Legend.svelte"
	import inc1960 from "./data/1960.geo.json";
	import inc1970 from "./data/1970.geo.json";
	import inc1980 from "./data/1980.geo.json";
	import inc1990 from "./data/1990.geo.json"
	import inc2000 from "./data/2000.geo.json";
	import inc2010 from "./data/2010.geo.json";
	import inc2020 from "./data/2020.geo.json";


	let coloursDiv = ["#DC4633", "#ee9d78", "#f2dfce", "#7eb4b3", "#007fa3"];
	let coloursSeq = ['#f2dfce','#ecb4a2','#e5816f','#dc4633','#ed1b00'];
	let spacing = [50, 100, 150, 200, 250]

	const avg_hhld_inc_2020 = 110000;
	const avg_ind_inc_2020 = 60000;
	const pov_lim_2020 = 18;	

	$: currentLayer = "hhld_inc";	

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




<Top />

<main>

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
		
		<h3>A first look at 2020 income data collected as part of the 2021 census</h3>
		<div id="mini-line"></div>
	</div>


	<div class="text">
		<p>On. Here's a map of the City of Toronto showing three pertinent variables</p>
	</div>

	<div id="top-map">
		<div class="layer-button-wrapper">
			<button 
			class:selected="{currentLayer === 'hhld_inc'}"
			class:not-selected="{currentLayer !== 'hhld_inc'}"
			on:click="{() => currentLayer = 'hhld_inc'}"
			id="hhld_inc">Average Household Income</button>
		
			<button 
			class:selected="{currentLayer === 'ind_inc'}"
			class:not-selected="{currentLayer !== 'ind_inc'}"
			on:click="{() => currentLayer = 'ind_inc'}" id="ind_inc">Average Individual Income</button>

			<button 
			class:selected="{currentLayer === 'pov_lim'}"
			class:not-selected="{currentLayer !== 'pov_lim'}"
			on:click="{() => currentLayer = 'pov_lim'}"  id="pov_lim">Poverty Rate</button>
		</div>
		
		<div class="mapBig">
			<MapTop coloursD = {coloursDiv} coloursS = {coloursSeq} currentLayer={currentLayer}/>
		</div>
	</div>

	<div class="top-info">
		<div class="legend">
			<Legend 
				colours = {coloursDiv}
				title1 = {"Census tract average household income relative"}
				title2 = {"to the City of Toronto's average for the year:"}
				labels = {[
					"Very Low Income (less than 70%)",
					"Low Income (70% to 85%)",
					"Middle Income (85% to 115%)",
					"High Income (115% to 130%)",
					"Very High Income (more than 130%)"
				]}	
			/>
		</div>
		<div class="big-number-box">
			<div class="big-number">
				<div class="big-number-number">$	{avg_hhld_inc_2020.toLocaleString("en-US")}</div>
				<div class="big-number-label">Average Household Income</div>
			</div>
		</div>
	</div>

	
	<div class="text">
		<p>For the six decades prior, clearly showing how lower-income neighbourhoods were once clustered in the centre.</p>
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
			<MapMini year={"2020"} tracts={inc2020.features} colours = {coloursDiv}  variable={"ii16"}/>
		</div>
		<div class="legend">
			<Legend 
				colours = {coloursDiv}
				title1 = {"Census tract average household income relative"}
				title2 = {"to the City of Toronto's average for the year:"}
				labels = {[
					"Very Low Income (less than 70%)",
					"Low Income (70% to 85%)",
					"Middle Income (85% to 115%)",
					"High Income (115% to 130%)",
					"Very High Income (more than 130%)"
				]}	
			/>
		</div>
	</div>


	<div class="text">
		<p>Indeed meow meow</p>
	</div>

	<div id="mini-line"></div>

	<div class="text">
		<p>Indeed meow meow</p>
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
		width: 100%;
		margin-top: 100px;
		text-align: center;
		font-family: "Source Serif Pro", serif;
	}

	#mini-line {
		margin: auto;
		width: 220px;
		height: 1px;
		background-color: black;
	}

	.text {
		font-family: "Source Serif Pro", serif;
		font-size: 19px;
		margin: auto;
		max-width: 600px;
		width: 100%;
		padding-top: 25px;
		padding-bottom: 25px;
		line-height: 160%;
	}

	.layer-button-wrapper {
		margin: auto;
		max-width: 600px;
		width: 100%;
	}
	.layer-button-wrapper button {
		border: solid 1px rgb(176, 176, 176);
		font-family: 	-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		cursor: pointer;
		border-radius: 1px;
		padding: 4px;
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

	.top-info {
		margin: auto;
		max-width: 820px;
		width: 100%;
		display: grid;
		gap: 10px 10px;
		grid-template-columns: repeat(2, 1fr);
	}

	.legend {
		margin: auto;
		max-width: 400px;
	}

	.mapGrid {
		margin: auto;
		max-width: 820px;
		width: 100%;
		display: grid;
		gap: 10px 10px;
		grid-template-columns: repeat(2, 1fr);
	}

	@media (max-width:820px) {
		.mapGrid {
			grid-template-columns: repeat(1, 1fr);
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

	
	
</style>

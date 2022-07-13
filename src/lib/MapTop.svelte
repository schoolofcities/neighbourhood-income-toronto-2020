<script>	
	
	import formerMun from "../data/formerMun.geo.json";
	import subwayLines from "../data/subwayLines.geo.json";
	import subwayStations from "../data/subwayStations.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";
	import tracts2020 from "../data/2020.geo.json";

	export var coloursD;	
	export var coloursSR;
	export var coloursSB;
	export var currentLayer;

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = innerWidth * 40/80

	// let c1 = [-79.29, 43.70]
	// let c2 = [-78.89, 43.64]
	// [-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ]
	// let c600 = [-79.145,43.68]

	$: projection = geoMercator()
		.center([-78.17 - 0.0023*innerWidth + 0.000001125*innerWidth**2, 43.5 + 0.00045*innerWidth - 2.5e-7*innerWidth**2])
		.scale([75000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);
	
	const params =	{
		"hhld_inc": {
			"name": "Household Income Average",
			"var_name": "aiath20",
			"colours": coloursD,
			"ref_point": 96000 
		},	
		"ind_inc": {
			"name": "Individual Income Average",
			"var_name": "aiati20",
			"colours": coloursD,
			"ref_point": 49080
		},
		"pov_lim": {
			"name": "Poverty Rate LIM",
			"var_name": "limat21",
			"colours": coloursSR,
			"ref_point": 13.2
		},
		"hhld_inc_m": {
			"name": "Household Income Median",
			"var_name": "miath20",
			"colours": coloursD,
			"ref_point": 74000 
		},	
		"ind_inc_m": {
			"name": "Individual Income Median",
			"var_name": "miati20",
			"colours": coloursD,
			"ref_point": 36000
		},
		"pop_den": {
			"name": "Population Density",
			"var_name": "p21",
			"colours": coloursSB,
			"ref_point": 4428	
		}
	}

	$: colorDiv = [];
	$: if (currentLayer === "pop_den") {
		colorDiv = scaleThreshold()
		.domain([1000,4000,7000,10000])
		.range(coloursSB);
	} else if (currentLayer === "pov_lim") {
		colorDiv = scaleThreshold()
		.domain([10,15,20,25])
		.range(coloursSR);
	} else if (currentLayer === "hhld_inc_m") {
		colorDiv = scaleThreshold()
		.domain([55000,70000,85000,100000])
		.range(coloursD);
	}  else if (currentLayer === "hhld_inc") {
		colorDiv = scaleThreshold()
		.domain([75000,90000,100000,115000])
		.range(coloursD);
	}  else if (currentLayer === "ind_inc") {
		colorDiv = scaleThreshold()
		.domain([35000,50000,65000,80000])
		.range(coloursD);
	} else if (currentLayer === "ind_inc_m") {
		colorDiv = scaleThreshold()
		.domain([30000,40000,50000,60000])
		.range(coloursD);
	}
	else {
		colorDiv = scaleThreshold()
		.domain([
			params[currentLayer]["ref_point"] * 0.8,
			params[currentLayer]["ref_point"] * 0.9,
			params[currentLayer]["ref_point"] * 1.1,
			params[currentLayer]["ref_point"] * 1.2,
		])
		.range(coloursD);
	}

	$: attributeName = params[currentLayer]["var_name"]

	$: features = tracts2020.features;
		
	$: features.map(item => {
		if (currentLayer !== "pop_den") {
			item.properties[attributeName]	
			? (item.properties.colour = colorDiv(item.properties[attributeName]))
			: (item.properties.colour = "white");
		} else {
			item.properties[attributeName]	
			? (item.properties.colour = colorDiv(item.properties[attributeName] / item.properties["landarea"]))
			: (item.properties.colour = "white");
		}
			
	});
	
	$: placeLabel = true;
	function labelToggle() {
		placeLabel = !placeLabel;
	}
	$: if (divWidth < 800) {
		placeLabel = false
	}
</script>



<div id="container" class="svg-container" bind:offsetWidth={divWidth}>

	<div id="labels">
		<button 
		id="label-button"
		class:label-selected="{placeLabel}"
		class:label-off="{divWidth < 800}"	
		on:click={labelToggle}>
			Labels
		</button>		
	</div>

	<svg width={innerWidth} height={height}	>
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}
		{#key attributeName}
		{#each features	as data}
			<path id="ct" d={path(data)} fill={data.properties.colour} />
		{/each}
		{/key}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}
		
		{#each subwayLines.features as data}
			<path id="subway-lines" d={path(data)} />
		{/each}
		{#each subwayStations.features as data}
			<circle
			class="subway-stop"
			cx={projection(data.geometry.coordinates)[0]}
			cy={projection(data.geometry.coordinates)[1]}
			r="2px"
			fill="black" />
		{/each}

		{#if placeLabel}	
			<text id="place-label" x="301" y="88">North York</text>
			<text id="place-label" x="389" y="243">East York</text>
			<text id="place-label" x="227" y="207">York</text>
			<text id="place-label" x="89" y="228">Etobicoke</text>
			<text id="place-label" x="519" y="163">Scarborough</text>
			<text id="place-label" x="297" y="287">Toronto</text>
		{/if}
	</svg>
	
</div>
	
<style>
	#container {
		width: 100%;
		max-width: 800px;
		min-width: 400px;
	}
	#fm-back {
		stroke: rgb(0, 0, 0);
		stroke-width: 5px;
		opacity: 0.08;
		fill-opacity: 0;
	}
	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
	#fm {
		stroke: rgb(36, 36, 36);
		stroke-width:1 px;
		fill-opacity: 0;
	}
	#subway-lines {
		fill-opacity: 0;
		stroke: rgb(0, 0, 0);
		stroke-width: 2px;
	}

	#place-label {
		font-size: 15px;
		fill: rgb(0, 0, 0);
		paint-order: stroke;
		stroke: #fff;
		stroke-opacity: 0.85;
		stroke-width: 4px;
		stroke-linecap: butt;
		stroke-linejoin: miter;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	#label-button {
		float: right;
		position: absolute;
		top: 25px;
		right: 20px;
		border: solid 1px rgb(176, 176, 176);
		font-family: 	-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		color:  rgb(103, 103, 103);
		cursor: pointer;
		border-radius: 1px;
		padding: 4px;
	}
	#label-button:hover {
		color: #007fa3;
	}
	.label-selected {
		background-color: rgb(255, 255, 255);
	}
	.label-off {
		display: none;
	}
</style>

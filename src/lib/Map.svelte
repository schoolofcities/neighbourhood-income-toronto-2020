<script>	
	
	import formerMun from "../data/formerMun.geo.json";
	import subwayLines from "../data/subwayLines.geo.json";
	import subwayStations from "../data/subwayStations.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export var year;
	export var tracts;
	export var colours;
	export var type;

	console.log(type)

	const avgInc = {
		"1960": 4307,
		"1970": 11748,
		"1980": 27476,
		"1990": 54601,
		"2000": 69125,
		"2010": 87038
	};

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = innerWidth * 40/80

	// let c1 = [-79.29, 43.70]
	// let c2 = [-78.89, 43.64]

	$: projection = geoMercator()
		.center([-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ])
		.scale([75000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);
	
	var color = scaleThreshold()
		.domain([
			avgInc[year] * 0.7,
			avgInc[year] * 0.85,
			avgInc[year] * 1.15,
			avgInc[year] * 1.3,
		])
		.range(colours);

	tracts.map((item) => {
		item.properties.avg_inc
			? (item.properties.color = color(item.properties.avg_inc))
			: (item.properties.color = "white");
	});

	let placeLabel = true;
	function labelToggle() {
		placeLabel = !placeLabel;
	}
</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>

	{#if type == "main"}
		<div id="labels">
			<button 
			id="label-button"
			class:selected="{placeLabel}"	
			on:click={labelToggle}>
				Labels
			</button>			
		</div>
	{/if}

	<svg width={innerWidth} height={height} id="meow">
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}
		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color} />
		{/each}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}
		{#if type == "smallMultiple"}
			<text id="year-label" x="5" y="22">{year}</text>
		{/if}
		{#if type == "main"}
			{#each subwayLines.features as data}
				<path id="subway-lines" d={path(data)} />
			{/each}
			{#each subwayStations.features as data}
				{console.log(data.geometry.coordinates)}
				<circle
				class="subway-stop"
				cx={projection(data.geometry.coordinates)[0]}
				cy={projection(data.geometry.coordinates)[1]}
				r="2px"
				fill="black" />
			{/each}
		{/if}

		{#if type == "main" && placeLabel}
			{console.log(type, placeLabel)}
			
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
	/* #meow {
		border: solid 1px rgb(243, 232, 232);
		border-bottom-right-radius: 100px;
	} */
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
	#subway-stops {
		fill-opacity: 1;
	}
	#year-label {
		font-size: 14px;
		fill: rgb(103, 103, 103);
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	#place-label {
		font-size: 15px;
		fill: rgb(0, 0, 0);
		font-weight: bold;
		paint-order: stroke;
		stroke: #fff;
		stroke-opacity: 0.55;
		stroke-width: 4px;
		stroke-linecap: butt;
		stroke-linejoin: miter;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	#label-button {
		float: right;
		margin-right: 87px;
		/* background-color: white; */
		border: solid 1px rgb(176, 176, 176);
		font-family: 	-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		color:  rgb(103, 103, 103);
		cursor: pointer;
		border-radius: 10px;
		padding: 4px;
		margin-bottom: -10px;
	}
	#label-button:hover {
		color: #007fa3;
	}
	.selected {
		background-color: rgb(255, 255, 255);
	}
</style>

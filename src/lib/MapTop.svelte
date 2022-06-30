<script>
	import formerMun from "../data/formerMun.geo.json";
	import subwayLines from "../data/subwayLines.geo.json";
	import subwayStations from "../data/subwayStations.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";

	export var year;
	export var tracts;
	export var colours;
	export var type;
	export var variable;

	const avgInc = {
		"1960": 4307,
		"1970": 11748,
		"1980": 27476,
		"1990": 54601,
		"2000": 69125,
		"2010": 87038,
		"2020": 109480, // actually 2016
	};

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = (innerWidth * 40) / 80;

	// let c1 = [-79.29, 43.70]
	// let c2 = [-78.89, 43.64]
	// [-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ]
	$: projection = geoMercator()
		.center([-79.426, 43.72])
		.scale([(80000 * innerWidth) / 800])
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
		item.properties[variable]
			? (item.properties.color = color(item.properties[variable]))
			: (item.properties.color = "white");
	});

	$: placeLabel = true;
	function labelToggle() {
		placeLabel = !placeLabel;
	}
	$: if (divWidth < 800) {
		placeLabel = false;
	}
</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	{#if type == "main"}
		<div class="layer-button">
			<button>Average Household Income</button>

			<button>Average Individual Income</button>

			<button>Poverty Rate</button>
		</div>

		<div id="labels">
			<button
				id="label-button"
				class:label-selected={placeLabel}
				class:label-off={divWidth < 800}
				on:click={labelToggle}
			>
				Labels
			</button>
		</div>
	{/if}

	<svg width={innerWidth} {height}>
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}
		{#each tracts as data}
			<path id="ct" d={path(data)} fill={data.properties.color} />
		{/each}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}
		{#if type == "main"}
			{#each subwayLines.features as data}
				<path id="subway-lines" d={path(data)} />
			{/each}
			{#each subwayStations.features as data}
				<circle
					class="subway-stop"
					cx={projection(data.geometry.coordinates)[0]}
					cy={projection(data.geometry.coordinates)[1]}
					r="2px"
					fill="black"
				/>
			{/each}
		{/if}

		{#if type == "main" && placeLabel}
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
		max-width: 1200px;
		min-width: 400px;
		border: 1px solid grey;
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
		stroke-width: 1 px;
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
		font-weight: bold;
		paint-order: stroke;
		stroke: #fff;
		stroke-opacity: 0.55;
		stroke-width: 4px;
		stroke-linecap: butt;
		stroke-linejoin: miter;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
	#label-button {
		float: right;
		margin-right: 87px;
		/* background-color: white; */
		border: solid 1px rgb(176, 176, 176);
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
		color: rgb(103, 103, 103);
		cursor: pointer;
		border-radius: 10px;
		padding: 4px;
		margin-bottom: -10px;
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

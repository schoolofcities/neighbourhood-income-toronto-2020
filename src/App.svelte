<script>

	import Top from "./lib/TopSofC.svelte";
	import Map from "./lib/Map.svelte";

</script>


<Top />
<main>
	
	<div class="title">
		<h1>Hello</h1>
	</div>
	<div class="mapBig">
		<Map />
	</div>
	<div class="text">
		<p>Hello</p>
	</div>
	<div class="mapSmall">
		<b>1961</b>
		<Map />
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
		background-color: rgb(255, 255, 255);
	}

	main {
		margin: 0 auto;
		width: 100%;
		position: relative;
	}

	.title {
		margin: auto;
		max-width: 600px;
		width: 100%;
		margin-top: 70px;
	}

	.text {
		margin: auto;
		max-width: 600px;
		width: 100%;
	}

	.mapBig {
		margin: auto;
		max-width: 800px;
	}

	.mapSmall {
		margin: auto;
		max-width: 400px;
	}
	
</style>

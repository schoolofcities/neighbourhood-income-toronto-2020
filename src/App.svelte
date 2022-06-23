<script>

	import Top from "./lib/TopSofC.svelte";
	import Map from "./lib/Map.svelte";

</script>

<main>
	<Top />
	<Map />
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
	
</style>

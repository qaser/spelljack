NUM_VARIATIONS = 1
NUM_VARIATIONS_ACTION = 2

ENVIRONMENT_THEMES = {
    "dark_fantasy": "shadowy ancient woods shrouded in thick mist, crumbling eerie castle silhouette under pale blue moonlight, glowing ethereal runes etched on twisted trees, subtle silhouettes of tattered cloaks and lurking mystical creatures, atmospheric fog rolling across uneven ground, high contrast cinematic lighting, dark moody tones, intricate details, SDXL optimized",
    "greek_mythology": "majestic marble columns in olive groves with golden laurel wreaths scattered, distant Mount Olympus peak under azure skies, ancient ruins with flowing toga fabrics draped over statues, warm sunlight filtering through leaves, classical symmetry, vibrant yet serene colors, high detail architecture, mythological aura, SDXL optimized",
    "gothic_victorian": "foggy cobblestone streets lit by flickering gas lamps, haunted Victorian manor with towering spires, velvet dresses and intricate lace details in shadowed doorways, candlelight glowing from arched windows, sepia-toned atmosphere, ornate ironwork, moody overcast sky, intricate textures, SDXL optimized",
    "succubus_lair": "opulent chamber with crimson velvet drapes and dark flickering candles, seductive shadows cast by gothic arches, glowing red embers in a ornate fireplace, silk sheets on a four-poster bed, forbidden allure with subtle demonic motifs, warm seductive lighting, rich jewel tones, high detail fabrics, SDXL optimized",
    "pirate_cove": "sandy tropical beach with weathered pirate ship anchored offshore, buried treasure chests half-exposed, swaying palm trees against crashing ocean waves, Jolly Roger flags fluttering in breeze, rum barrels stacked near campfires, golden sunset hues, adventurous salty air vibe, detailed wood grains, SDXL optimized",
    "chinese_fantasy": "ethereal jade palaces amid blooming cherry blossoms, silk-robed figures near majestic dragon statues, misty layered mountains in background, hanging red lanterns and intricate calligraphy scrolls, soft diffused lighting, vibrant greens and pinks, mystical harmony, high detail architecture, SDXL optimized",
    "japanese_onsen": "steaming hot springs surrounded by bamboo screens and falling cherry blossoms, folded kimonos on rocks, stone lanterns along misty wooden bridges, tranquil fog rising from water, soft pastel dawn light, serene natural textures, zen minimalism, SDXL optimized",
    "slavic_fantasy": "frost-covered dense forests with wooden izba hut glowing from within, fur-clad silhouettes by roaring fire, ancient glowing runes on bark, vast snowy plains under overcast sky, folklore creatures in distant mist, cold blue tones, intricate wood carvings, atmospheric chill, SDXL optimized",
    "arcane_arena": "circular arena etched with magical sigils and floating iridescent crystals, glowing portals swirling with energy, enchanted armor displays on pedestals, starry night sky overhead, mystical purple-blue energy auras, ancient relics scattered, dramatic volumetric lighting, high fantasy details, SDXL optimized",
    "shadow_realm": "endless dark void with ghostly translucent apparitions, twisted barren trees with glowing red eyes peering out, foggy abyssal chasm, shattered floating mirrors reflecting voids, eerie whispering winds visualized as subtle swirls, monochromatic blacks with crimson accents, surreal horror depth, SDXL optimized",
    "enchanted_boudoir": "intimate room with flowing silk curtains and ornate gilded mirrors, soft golden candlelight illuminating plush velvet cushions, floral perfume bottles on vanity, romantic pink and gold glow, intricate lace and fabric details, warm intimate atmosphere, high detail opulence, SDXL optimized",
    "roman_gladiator": "vast Colosseum arena, gladiator armor and shields propped against marble statues, cheering crowd blurred in tiered seats, laurel wreaths on podiums, stone arches under clear blue sky, dramatic sunlight shadows, historical grit, SDXL optimized",
    "high_fantasy": "lush elven forests with glowing cascading waterfalls, golden crowns on treetop thrones, mythical winged creatures soaring, enchanted ivy-covered castles, sparkling crystal-clear rivers, vibrant emerald and gold palette, magical particle effects, epic wide-angle view, SDXL optimized",
    "mystical_brothel": "dimly lit parlor with red hanging lanterns and silk tapestries on walls, ornate carved beds with velvet cushions, exotic perfume bottles and shadowy alcoves, seductive warm amber lighting, intricate gold filigree, mysterious allure, high detail textures, SDXL optimized",
    "magical_academy": "grand ancient library with towering spell books and floating glowing orbs, stained glass windows casting colorful patterns on wooden desks, starry enchanted ceiling above, mystical artifacts on shelves, soft magical blue hues, intricate book details, SDXL optimized",
    "dieselpunk": "gritty industrial skyline with rusty massive machinery and smoky factories, leather-jacketed figures near vintage armored cars, brass goggles reflecting sepia-toned exhaust, overcast polluted sky, mechanical gears and pipes, retro-futuristic grit, high detail metalwork, SDXL optimized",
    "cyberpunk_redlight": "rain-slicked neon-lit streets with holographic ads flickering, dark alleys lined with leather-clad crowds, glowing cybernetic implants on exposed skin, urban nightlife buzz under perpetual night, vibrant pink-blue neons, reflective puddles, high-tech dystopia, SDXL optimized",
    "forbidden_temple": "overgrown ancient stone ruins with twisting vines and golden idols in torchlit chambers, intricate carvings on walls, mystical green fog drifting through hidden archways, dim warm firelight, mysterious tropical humidity, detailed erosion textures, SDXL optimized",
    "victorian_steampunk": "foggy cobblestone streets with clockwork gears and brass steam pipes protruding from buildings, corseted figures in top hats near vintage laboratories, steam engines puffing smoke, warm brass and copper tones, intricate mechanical details, retro industrial charm, SDXL optimized",
    "sexual_teacher": "cozy classroom with chalkboard covered in equations, wooden desk cluttered with books, glasses and tight blouse on chair, towering bookshelves in dim lamplight, scholarly seduction vibe with subtle erotic undertones, warm intimate lighting, detailed wood and fabric, SDXL optimized",
    "maid_fantasy": "grand Victorian mansion interior with frilly-aproned uniforms on hooks, feather dusters near polished marble floors, lace stockings draped over furniture, playful elegant atmosphere with vintage ornate details, soft daylight through windows, high detail lacework, SDXL optimized",
    "urban_fantasy_office": "sleek high-rise office with neon cityscape view through floor-to-ceiling windows, modern glass desk with glowing magical artifacts, leather armchairs and holographic screens, urban magic fusion in twilight blues, futuristic yet mystical, detailed reflections, SDXL optimized",
    "ancient_egyptian": "vast golden sand dunes with hieroglyph-covered obelisks and ankh symbols etched in stone, pharaoh's tomb entrance near palm-fringed Nile River, scorching sun casting long shadows, warm ochre and gold palette, ancient monumental scale, SDXL optimized",
    "celtic_druid": "misty ancient oak groves with moss-covered standing stones and druidic runes glowing faintly, woven cloaks on branches, bonfires in sacred clearings, earthy green-brown tones, ethereal fog, natural organic textures, SDXL optimized",
    "aztec_pyramid": "stepped stone pyramids enveloped in jungle vines, golden jaguar masks and feathered headdresses on altars, sacrificial stone slabs under tropical sun, vibrant greens and golds, intricate glyph carvings, humid exotic atmosphere, SDXL optimized",
    "samurai_dojo": "spacious tatami-floored room with cherry blossoms visible through paper screens, katana swords racked on bamboo walls, zen rock garden outside, disciplined warm sunlight filtering in, minimalist elegant lines, high detail wood grains, SDXL optimized",
    "cowboy_saloon": "rustic wooden saloon with swinging doors and whiskey bottles on bar, dusty cowboy hats on hooks, poker tables under desert sunset glow through windows, warm earthy tones, weathered wood textures, Western charm, SDXL optimized",
    "horror_mansion": "decaying grand mansion with creaky wooden floors and cobwebs draping broken chandeliers, shadowy endless halls with cracked mirrors, ghostly apparitions in stormy night lightning, cold desaturated colors, eerie volumetric fog, detailed decay, SDXL optimized",
    "fairy_tale_castle": "whimsical ivory towers rising from enchanted rose gardens, golden gates and sparkling chandeliers inside, flowing gowns on balconies overlooking forest, magical soft pink glow, fairytale wonder, intricate floral details, SDXL optimized",
    "volcanic_forge": "fiery cavern with molten lava rivers and glowing red anvils, obsidian walls reflecting sparks, forged weapons on racks amid smoky intense heat, dramatic orange-red lighting, rugged volcanic textures, SDXL optimized",
    "ice_palace": "crystalline palace with frosted glass walls and icicle chandeliers, snowy expansive landscapes outside, fur cloaks on thrones near frozen lakes, cool blue ethereal glow, pristine icy details, SDXL optimized",
    "desert_nomad": "rolling golden dunes with Bedouin tents and camel silhouettes at starry night oasis, woven rugs around pools, flowing scarves in wind, warm amber and deep blue palette, nomadic tranquility, detailed sand ripples, SDXL optimized",
    "medieval_tavern": "cozy stone-walled tavern with wooden long tables and ale mugs, flickering candlelight on rustic beams, bard's lute in corner, hearty warm fire glow, earthy browns, lived-in textures, SDXL optimized",
    "renaissance_court": "opulent marble halls with velvet-draped thrones and golden crowns, ornate gowns in grand chandeliers' light, lute musicians in corners, royal elegant golds and reds, intricate tapestries, SDXL optimized",
    "industrial_revolution": "smoky factory interiors with massive iron gears and steam trains outside, worker caps on benches amid cobblestone streets, oil lanterns casting gritty shadows, sepia industrial haze, mechanical details, SDXL optimized",
    "mushroom_forest": "surreal forest of giant colorful mushrooms with glowing spore clouds, misty twisted vines and fairy lights twinkling, enchanted creatures in undergrowth, vibrant psychedelic hues, ethereal bioluminescent glow, SDXL optimized",
    "desert_oasis": "lush palm-fringed turquoise pools amid golden sands, silk tents under starry skies with exotic blooming flowers, tranquil serene blues and golds, reflective water surfaces, SDXL optimized",
    "bamboo_forest": "dense tall bamboo groves with misty winding stone paths, koi ponds and paper lanterns hanging, zen soft green tranquility, diffused sunlight filtering through leaves, natural minimalism, SDXL optimized",
    "northern_lights": "vast snowy plains under dancing aurora borealis and starry skies, fur-clad figures on icy cliffs, mystical green-purple glow on horizons, cold crisp air vibe, ethereal northern beauty, SDXL optimized",
    "baroque_opera": "grand gilded opera house with velvet stage curtains and crystal chandeliers, ornate balconies with powdered wigs, candlelit 17th-century stage, gold leaf details and dramatic shadows, theatrical opulent ambiance, SDXL optimized",
    "ming_dynasty_garden": "serene Chinese scholar's garden with moon gates and koi ponds amid willow trees, lacquered pavilions with silk scrolls and porcelain vases, bamboo groves and lotus blooms, soft harmonious lighting, intricate classical details, SDXL optimized",
    "viking_longhouse": "rugged timber longhouse with animal pelts and roaring central hearth, carved Norse runes on walls, mead horns on wooden benches under torchlight, smoky warm atmosphere, authentic Nordic textures, SDXL optimized",
    "renaissance_venice": "romantic canals with gondolas gliding past marble palaces, carnival masks on bridges like Bridge of Sighs, gold leaf mosaics and velvet gowns in candlelit reflections, watery Renaissance mystery, vibrant blues and golds, SDXL optimized",
    "art_deco_speakeasy": "hidden 1920s speakeasy with geometric gold-trimmed black marble walls, jazz band on stage amid cigarette smoke, velvet ropes and crystal glasses, ziggurat chrome fixtures, glamorous art deco luxury, SDXL optimized",
    "rococo_salon": "elegant French salon in pastel hues with curved ornate furniture and floral-patterned walls, intricate mirrors and delicate china, silk drapery with playful cherubs, lighthearted gold scrollwork, whimsical luxury, SDXL optimized",
    "ottoman_harem": "lavish chamber with colorful mosaic tiles and silk cushions around hookah pipes, lattice screens over mosaic fountains, incense smoke and gold jewelry on exotic fabrics, mysterious palace intrigue, warm exotic tones, SDXL optimized",
    "byzantine_basilica": "majestic basilica with shimmering gold mosaics and religious icons on marble floors, domed architecture with incense and candlelight, sacred deep blue-gold devotion, mystical atmospheric depth, SDXL optimized",
    "tudor_palace": "Tudor palace with half-timbered walls and rich tapestries, oak-beamed rooms with leaded windows overlooking herb gardens, stone fireplaces and royal portraits, Renaissance courtly intrigue, warm historical tones, SDXL optimized",
    "silk_road_caravanserai": "bustling desert oasis caravanserai with camel trains and colorful spice market rugs, lantern-lit starry nights with exotic multicultural traders, ancient Silk Road mystery, warm sandy hues, detailed fabrics, SDXL optimized",
    "middle_earth": "epic misty mountains and ancient elven forests with glowing runes on stone bridges, rolling green hills and enchanted rivers, ethereal Tolkien light through forgotten ruins, high fantasy immersion, SDXL optimized",
    "narnia": "magical Narnia wardrobe entrance to snow-covered lampposts and frozen waterfalls, talking trees around stone table, Cair Paravel castle in thawing eternal winter, golden royal light with creatures, whimsical wonder, SDXL optimized",
    "westeros": "grim medieval Westeros with stark castles like Winterfell crypts and Iron Throne in Red Keep, weirwood trees and stormy seas, dragon skulls and Dornish gardens, fiery shadowy Game of Thrones vibe, detailed stonework, SDXL optimized",
    "hogwarts": "enchanted Hogwarts castle with moving staircases and floating candles in Great Hall, starry enchanted ceiling over potions classroom, Forbidden Forest and Quidditch pitch at twilight, magical Harry Potter artifacts, whimsical mystery, SDXL optimized",
    "discworld": "quirky Discworld Ankh-Morpork bustling streets and Unseen University library, witch cottages in Ramtop mountains, surreal humorous magic with patrician's palace, vibrant fantastical details, SDXL optimized",
    "dune": "harsh Arrakis desert with spice sandstorms and sietch cave entrances, sandworm tracks under burning sun, Fremen stillsuits near imperial palace, melange visionary haze and crysknife glints, epic sci-fi aridity, SDXL optimized",
    "gormenghast": "melancholic Gormenghast gothic castle with crumbling towers and endless ritual corridors, dusty libraries and rain-slicked stone courtyards, shadowy ancient traditions, moody desaturated tones, SDXL optimized",
    "his_dark_materials": "mystical His Dark Materials world with northern lights over armored bear ice palace, Bolvangar ruins and Oxford colleges, zeppelin shadows with dust particles and multiverse windows, ethereal fantasy depth, SDXL optimized",
    "earthsea": "archipelagic Earthsea islands with dragon-perched mountains and wizard school towers, dry stone walls along sailing ships, naming magic in tidal patterns under star navigation, oceanic mystical lore, SDXL optimized",
    "alice_wonderland": "surreal Alice in Wonderland with oversized mushrooms and mad tea party tables, Queen's croquet ground with talking flowers, mirror distortions and playing card motifs, dreamlike curious proportions, vibrant whimsy, SDXL optimized",
    "metal_concert": "intense metal concert mosh pit with strobe lights and laser beams cutting through smoke, stage diving near amplifier stacks and drum kits, leather jackets and spikes in chaotic energy, high-contrast dynamic lighting, SDXL optimized",
    "warhammer_40k": "grimdark Warhammer 40k gothic spaceship cathedrals with imperial aquila skulls and plasma reactors, adamantium structures with purity seals in incense smoke, eternal war xenotech artifacts, dark futuristic horror, SDXL optimized",
    "norse_mythology": "mythic Norse realms with Yggdrasil world tree roots in frozen fjords, Valhalla mead hall and runestone circles under northern lights, longship prows and frost giant peaks, bifrost rainbow glow, epic Viking saga, SDXL optimized",
    "atompunk": "retro atompunk atomic age with curved plastic furniture in geodesic domes, nuclear symbols and vacuum tube glows in fallout shelters, chrome space-age designs with radiation optimism, vintage futuristic palette, SDXL optimized",
    "napoleonic_era": "dramatic Napoleonic battlefield with smoke from cannon barrages, military tents and stacked muskets in European fields, officer maps and uniform jackets near cavalry saddles, imperial war elegance, historical grit, SDXL optimized",
    "ww1_aviation": "early 20th-century WW1 biplane hangars with propeller details and leather caps, machine guns on vintage cockpits amid aerial cloud dogfights, oil-stained trenches below, sepia aviation adventure, SDXL optimized",
    "spy_thriller": "tense spy thriller penthouse with classified docs and hidden cameras, laser grids over casino tables with champagne, trench coats in shadowy encrypted meetings, noir danger and seduction, high-contrast film noir, SDXL optimized",
}

CLOTHING_BY_THEME = {
    "metal_concert": {
        "dress": [
            "band t-shirt with rolled sleeves, comfortable fit",
            "leather skirt with buckles, practical style",
            "corset-style top with laces, sturdy design",
            "mesh long-sleeve shirt, layered look"
        ],
        "lingerie": [
            "simple cotton bra, everyday wear",
            "leather belt harness, functional accessory",
            "basic undergarments with studs",
            "mesh undershirt, breathable fabric"
        ],
        "accessories": [
            "spiked wristbands, bold statement",
            "chain necklace, simple pendant",
            "fingerless gloves, protective",
            "metal stud earrings"
        ],
        "stockings": [
            "fishnet stockings, patterned",
            "thigh-high socks with stripes",
            "leather leg wraps",
            "leggings with prints"
        ],
        "colors": ["black", "blood red", "metal silver", "neon"]
    },
    "warhammer_40k": {
        "dress": [
            "imperial guard uniform, buttoned jacket",
            "sororitas armor plating, protective gear",
            "mechanicus robes, hooded cloak",
            "gothic dress with symbols, formal wear"
        ],
        "lingerie": [
            "cotton undergarments with seals",
            "mesh undersuit, durable material",
            "leather straps, supportive",
            "silk shift with patterns"
        ],
        "accessories": [
            "aquila pendant necklace",
            "power tool belt",
            "rosarius medallion",
            "augmetic arm brace"
        ],
        "stockings": [
            "armored leg guards",
            "lace leg covers with emblems",
            "mesh leg wraps",
            "tattooed leg designs"
        ],
        "colors": ["imperial red", "gothic black", "gold", "steel grey"]
    },
    "norse_mythology": {
        "dress": [
            "fur-trimmed tunic, laced sides",
            "chainmail vest, layered protection",
            "wool dress with embroidery",
            "valkyrie winged cloak, flowing"
        ],
        "lingerie": [
            "linen underdress, simple fit",
            "leather belt straps",
            "fur-lined undershirt",
            "painted body patterns"
        ],
        "accessories": [
            "torque neck ring",
            "arm cuffs with runes",
            "belt buckle carved",
            "feather hair clips"
        ],
        "stockings": [
            "wool leg wraps",
            "leather leg guards",
            "fur-trimmed boots",
            "tattooed leg motifs"
        ],
        "colors": ["forest green", "deep blue", "blood red", "natural brown"]
    },
    "atompunk": {
        "dress": [
            "vinyl jumpsuit, zipped up",
            "cocktail dress with prints",
            "shelter outfit, practical",
            "space age dress, structured"
        ],
        "lingerie": [
            "printed cotton bra",
            "silk shorts with symbols",
            "mesh undersuit",
            "tattooed designs"
        ],
        "accessories": [
            "goggles on head",
            "gas mask strap",
            "vintage watch",
            "plastic jewelry"
        ],
        "stockings": [
            "fishnet with patterns",
            "vinyl leg covers",
            "sheer stockings",
            "painted legs"
        ],
        "colors": ["atomic orange", "plastic yellow", "radiation green", "steel blue"]
    },
    "napoleonic_era": {
        "dress": [
            "empire waist gown, modest neckline",
            "military jacket over dress",
            "ball gown with sleeves",
            "riding habit skirt"
        ],
        "lingerie": [
            "chemise underdress",
            "corset with straps",
            "silk stockings",
            "lace undergarments"
        ],
        "accessories": [
            "sabre belt",
            "medal pins",
            "feathered hat",
            "opera gloves"
        ],
        "stockings": [
            "silk stockings with patterns",
            "sheer embroidered",
            "wool riding stockings",
            "bare under dress"
        ],
        "colors": ["imperial blue", "regal white", "military gold", "blood red"]
    },
    "metro_2033": {
        "dress": [
            "gas mask strap on uniform",
            "military uniform with patches",
            "makeshift dress from fabric",
            "leather jacket over layers"
        ],
        "lingerie": [
            "thermal underwear",
            "cotton bra under shirt",
            "mesh undersuit",
            "scarred skin"
        ],
        "accessories": [
            "ammunition belt",
            "filter canisters",
            "scrap jewelry",
            "knife sheath"
        ],
        "stockings": [
            "ripped tights",
            "wool socks",
            "leg wraps",
            "dirt-marked legs"
        ],
        "colors": ["concrete grey", "rust brown", "dirt black", "mushroom pale"]
    },
    "ww1_aviation": {
        "dress": [
            "leather flight jacket over shirt",
            "mechanic overalls buttoned",
            "period dress with motifs",
            "scarf tied neatly"
        ],
        "lingerie": [
            "silk chemise",
            "lace bra with designs",
            "stockings patterned",
            "oil-stained undershirt"
        ],
        "accessories": [
            "goggles on forehead",
            "flowing scarf",
            "flight cap",
            "map case"
        ],
        "stockings": [
            "wool stockings",
            "silk with clocks",
            "leather wraps",
            "bare legs"
        ],
        "colors": ["leather brown", "sky blue", "khaki", "blood red"]
    },
    "spy_thriller": {
        "dress": [
            "black dress with pockets",
            "trench coat closed",
            "evening gown modest",
            "catsuit zipped"
        ],
        "lingerie": [
            "cotton bodysuit",
            "silk chemise",
            "garter belt",
            "tattooed skin"
        ],
        "accessories": [
            "pistol holster",
            "microfilm pendant",
            "martini glass",
            "smoke device"
        ],
        "stockings": [
            "sheer stockings",
            "fishnets patterned",
            "opaque tights",
            "bare legs"
        ],
        "colors": ["spy black", "rouge red", "gold", "silver"]
    },
    "middle_earth": {
        "dress": [
            "elven gown with embroidery, long sleeves",
            "rohan riding dress, practical",
            "gondorian noble dress, layered",
            "hobbit dress with apron"
        ],
        "lingerie": [
            "silken chemise with patterns",
            "leather harness",
            "linen underdress",
            "mesh undersuit"
        ],
        "accessories": [
            "mithril necklace",
            "leather bracers",
            "cloak clasp",
            "hair vines"
        ],
        "stockings": [
            "silk stockings with patterns",
            "leather leg wraps",
            "wool stockings",
            "ankle bracelets"
        ],
        "colors": ["forest green", "silver gray", "deep blue", "earth brown"]
    },
    "narnia": {
        "dress": [
            "queen's gown with trim, modest",
            "dryad dress with leaves",
            "royal dress with pearls",
            "battle dress with leather"
        ],
        "lingerie": [
            "silk chemise patterned",
            "fur-lined corset",
            "sheer underdress",
            "velvet shorts"
        ],
        "accessories": [
            "gold crown",
            "ivory horn necklace",
            "leather gloves",
            "snowflake pins"
        ],
        "stockings": [
            "silk stockings patterned",
            "wool knitted",
            "sheer silver",
            "bare legs"
        ],
        "colors": ["icy white", "royal purple", "gold", "deep red"]
    },
    "westeros": {
        "dress": [
            "lannister gown with embroidery",
            "targaryen dress patterned",
            "stark dress with fur",
            "dornish silk dress"
        ],
        "lingerie": [
            "silk shift with sigils",
            "leather corset",
            "mesh underdress",
            "linen chemise"
        ],
        "accessories": [
            "dragon bone necklace",
            "metal hair chains",
            "leather belt",
            "fur stole"
        ],
        "stockings": [
            "silk with embroidery",
            "wool hose",
            "sheer metallic",
            "bare legs"
        ],
        "colors": ["crimson", "black", "grey", "gold"]
    },
    "hogwarts": {
        "dress": [
            "school uniform with robe",
            "yule ball gown shimmering",
            "professor's robes embroidered",
            "witch dress with hat"
        ],
        "lingerie": [
            "lace bra with details",
            "silk chemise crested",
            "mesh bodysuit patterned",
            "stockings enchanted"
        ],
        "accessories": [
            "wand holder",
            "time turner necklace",
            "spectacles",
            "prefect badge"
        ],
        "stockings": [
            "striped knee socks",
            "sheer with snitches",
            "opaque tights patterned",
            "bare under skirt"
        ],
        "colors": ["scarlet", "emerald", "blue", "yellow"]
    },
    "discworld": {
        "dress": [
            "witch's dress layered",
            "assassin's leathers",
            "ankh-morpork fashion ruffled",
            "uniform buttoned"
        ],
        "lingerie": [
            "cotton underthings",
            "lace with symbols",
            "silk with patterns",
            "mesh glowing"
        ],
        "accessories": [
            "pointed hat",
            "necklaces with charms",
            "pocket watch",
            "badge"
        ],
        "stockings": [
            "striped stockings",
            "black practical",
            "fishnets patterned",
            "bare legs"
        ],
        "colors": ["black", "purple", "ochre", "grey"]
    },
    "dune": {
        "dress": [
            "still suit elegant",
            "imperial gown patterned",
            "fremen desert dress",
            "bene gesserit robe"
        ],
        "lingerie": [
            "silk undergarments",
            "mesh bodysuit",
            "traditional underdress",
            "painted body"
        ],
        "accessories": [
            "crysknife sheath",
            "water rings",
            "desert goggles",
            "spice jewelry"
        ],
        "stockings": [
            "still suit leggings",
            "sheer desert style",
            "bare legs patterned",
            "leather wraps"
        ],
        "colors": ["desert orange", "spice blue", "black", "cream"]
    },
    "gormenghast": {
        "dress": [
            "gothic gown buttoned",
            "stone-colored dress",
            "ritual robe symbolic",
            "practical dress"
        ],
        "lingerie": [
            "linen chemise",
            "corset laced",
            "sheer underdress",
            "stockings patched"
        ],
        "accessories": [
            "key ring belt",
            "spectacles",
            "shawl patterned",
            "ritual dagger"
        ],
        "stockings": [
            "grey stockings",
            "wool practical",
            "black faded",
            "bare legs"
        ],
        "colors": ["stone grey", "dusty rose", "faded black", "parchment"]
    },
    "his_dark_materials": {
        "dress": [
            "scholastic skirt layered",
            "arctic exploration dress",
            "witch silk patterned",
            "oxford uniform"
        ],
        "lingerie": [
            "wool combinations",
            "silk chemise laced",
            "thermal underlayers",
            "bare with connection"
        ],
        "accessories": [
            "compass instrument",
            "fur hood",
            "books",
            "spyglass"
        ],
        "stockings": [
            "wool with garters",
            "silk evening",
            "practical tights",
            "bare legs"
        ],
        "colors": ["navy blue", "oxford grey", "arctic white", "burgundy"]
    },
    "earthsea": {
        "dress": [
            "archipelago wool dress",
            "wizard robe runed",
            "dragon rider leathers",
            "island native dress"
        ],
        "lingerie": [
            "linen underdress",
            "silk chemise patterned",
            "bare tattooed",
            "mesh with crystals"
        ],
        "accessories": [
            "carved staff",
            "shell necklace",
            "navigation tools",
            "name jewelry"
        ],
        "stockings": [
            "bare salt-sprayed",
            "wool leg wraps",
            "net stockings",
            "leather sandals"
        ],
        "colors": ["ocean blue", "storm grey", "sand beige", "deep green"]
    },
    "alice_wonderland": {
        "dress": [
            "blue pinafore neat",
            "queen gown patterned",
            "cheshire striped dress",
            "hatter tea dress layered"
        ],
        "lingerie": [
            "lace bloomers",
            "corset designed",
            "sheer chemise patterned",
            "stockings printed"
        ],
        "accessories": [
            "hair ribbon",
            "pocket watch chain",
            "teacup",
            "card fan"
        ],
        "stockings": [
            "striped mismatched",
            "white with stains",
            "sheer patterned",
            "bare legs"
        ],
        "colors": ["royal blue", "heart red", "cheshire pink", "mad purple"]
    },
    "silk_road_caravanserai": {
        "dress": [
            "silk harem pants belted",
            "embroidered vest closed",
            "caftan with slits modest",
            "wrap dress tied"
        ],
        "lingerie": [
            "coin belt hips",
            "bandeau embroidered",
            "pantaloons threaded",
            "silk sash top"
        ],
        "accessories": [
            "gold bangles arms",
            "nose chain earring",
            "ankle bracelets bells",
            "headscarf tied"
        ],
        "stockings": [
            "bare henna patterned",
            "silk leg wraps",
            "leather sandals",
            "gold ankle cuffs"
        ],
        "colors": ["spice orange", "saffron yellow", "lapis blue", "deep crimson"]
    },
    "tudor_palace": {
        "dress": [
            "corseted velvet gown neckline modest",
            "chemise through sleeves",
            "farthingale skirt closed",
            "embroidered kirtle laced"
        ],
        "lingerie": [
            "linen smock",
            "ribbon corset",
            "silk stockings",
            "embroidered partlet"
        ],
        "accessories": [
            "pearl necklace",
            "gable hood",
            "girdle belt pendant",
            "embroidered gloves"
        ],
        "stockings": [
            "silk with garters",
            "embroidered peeking",
            "wool hose",
            "linen sheer"
        ],
        "colors": ["Tudor rose red", "forest green", "royal purple", "cream"]
    },
    "baroque_opera": {
        "dress": [
            "corseted silk gown embroidered",
            "velvet opera dress cutouts modest",
            "chemise contained by corset"
        ],
        "lingerie": [
            "ribbon corset garters",
            "chemise embroidered",
            "lace tap pants"
        ],
        "accessories": [
            "opera gloves elbows",
            "pearl choker pendant",
            "feathered mask"
        ],
        "stockings": [
            "silk with garters",
            "lace with patterns",
            "nude embroidered"
        ],
        "colors": ["deep burgundy", "royal blue", "gold", "cream"]
    },
    "ming_dynasty_garden": {
        "dress": [
            "silk robe closed embroidered",
            "outer robe over inner dress",
            "high-waisted gown slits modest"
        ],
        "lingerie": [
            "silk underrobe tied",
            "binding cloth embroidered",
            "inner garments sheer"
        ],
        "accessories": [
            "jade hair pins",
            "gold chain necklace",
            "silk slippers"
        ],
        "stockings": [
            "silk with patterns",
            "embroidered gold",
            "transparent ankle ties"
        ],
        "colors": ["imperial yellow", "deep red", "jade green", "cream"]
    },
    "viking_longhouse": {
        "dress": [
            "fur-trimmed tunic laced",
            "leather dress clasped",
            "wool gown embroidered slit modest"
        ],
        "lingerie": [
            "linen underdress",
            "leather harness",
            "fur-lined undershirt"
        ],
        "accessories": [
            "torque necklace",
            "arm rings",
            "belt buckle runed"
        ],
        "stockings": [
            "wool leg wraps",
            "leather leg harness",
            "fur-trimmed boots"
        ],
        "colors": ["forest green", "deep blue", "blood red", "natural brown"]
    },
    "renaissance_venice": {
        "dress": [
            "corseted brocade gown decolletage modest",
            "velvet dress slashed sleeves",
            "partlet over shoulders"
        ],
        "lingerie": [
            "camicia embroidered",
            "lace corset ribbon",
            "silk stockings garters"
        ],
        "accessories": [
            "carnival mask",
            "pearl necklace",
            "gold chain belt"
        ],
        "stockings": [
            "silk with clocks",
            "embroidered gold",
            "black lace tops"
        ],
        "colors": ["crimson", "deep green", "gold", "black"]
    },
    "art_deco_speakeasy": {
        "dress": [
            "fringed flapper dress",
            "bias-cut silk gown",
            "beaded cocktail dress"
        ],
        "lingerie": [
            "lace teddy garters",
            "silk chemise lace",
            "step-ins embroidered"
        ],
        "accessories": [
            "pearl necklace wrapped",
            "feathered headband",
            "cigarette holder"
        ],
        "stockings": [
            "sheer back seams",
            "fishnet rhinestone",
            "silk clocks"
        ],
        "colors": ["black", "champagne", "emerald", "ruby red"]
    },
    "rococo_salon": {
        "dress": [
            "pastel silk gown laced",
            "chemise overdress",
            "corseted dress patterned"
        ],
        "lingerie": [
            "embroidered corset ribbons",
            "sheer chemise lace",
            "silk stockings garters"
        ],
        "accessories": [
            "fan coy",
            "powdered wig",
            "ribbon choker cameo"
        ],
        "stockings": [
            "silk floral",
            "sheer lace tops",
            "ribbon garters"
        ],
        "colors": ["powder blue", "blush pink", "cream", "gold"]
    },
    "ottoman_harem": {
        "dress": [
            "sheer trousers hemmed",
            "beaded bra top",
            "silk caftan closed"
        ],
        "lingerie": [
            "belly belt hips",
            "pantaloons gold thread",
            "beaded bra chains"
        ],
        "accessories": [
            "gold nose chain",
            "bracelets arms",
            "head scarf"
        ],
        "stockings": [
            "harem pants sheer",
            "leg bands embroidered",
            "bare ankle bracelets"
        ],
        "colors": ["sapphire", "ruby", "gold", "emerald"]
    },
    "byzantine_basilica": {
        "dress": [
            "gold lamé gown patterned",
            "purple silk embroidered",
            "veil over shoulders"
        ],
        "lingerie": [
            "silk chemise gold",
            "jeweled corset motifs",
            "underdress sheer"
        ],
        "accessories": [
            "gold collar chest",
            "jeweled belt hips",
            "veil cross brooch"
        ],
        "stockings": [
            "gold embroidered",
            "purple silk cross",
            "metallic sheer"
        ],
        "colors": ["imperial purple", "gold", "deep blue", "red"]
    },
    "dark_fantasy": {
        "dress": [
            "velvet gown embroidered runes",
            "leather corset dress overlays",
            "silk robe symbols"
        ],
        "lingerie": [
            "lace bralette panels",
            "satin thong chains",
            "mesh bodysuit edges"
        ],
        "accessories": [
            "silver collar pendant",
            "leather cuffs wrists",
            "dark veil shoulders"
        ],
        "stockings": [
            "lace rune patterns garters",
            "black mesh twilight",
            "silk chain garters"
        ],
        "colors": ["midnight black", "blood red", "deep violet"]
    },
    "greek_mythology": {
        "dress": [
            "silk tunic draped belt",
            "linen wrap motifs",
            "pleated chiton hems"
        ],
        "lingerie": [
            "silk bralette straps",
            "lace thong threads",
            "satin slip drapes"
        ],
        "accessories": [
            "gold armlet arm",
            "laurel circlet",
            "serpent bracelet"
        ],
        "stockings": [
            "silk gold filaments",
            "lace vine garters",
            "mesh olive designs"
        ],
        "colors": ["pure white", "sunlit gold", "Aegean blue"]
    },
    "gothic_victorian": {
        "dress": [
            "lace gown décolletage modest ribbons",
            "blouse over skirt ruffled",
            "brocade mini patterns hem"
        ],
        "lingerie": [
            "satin corset bralette frills",
            "lace panties laced",
            "mesh chemise lines"
        ],
        "accessories": [
            "velvet choker pearl",
            "silver locket bosom",
            "lace gloves elbows"
        ],
        "stockings": [
            "fishnet lace tops weave",
            "silk moody shades",
            "sheer Victorian motifs"
        ],
        "colors": ["raven black", "rich burgundy", "aged ivory"]
    },
    "succubus_lair": {
        "dress": [
            "silk slip backless shimmer",
            "velvet wrap knotted flow",
            "laced gown slits"
        ],
        "lingerie": [
            "satin bralette lace",
            "strappy thong",
            "chained mesh slip"
        ],
        "accessories": [
            "thorny choker interior",
            "anklet charm sway",
            "horn adornment"
        ],
        "stockings": [
            "thigh-highs garters",
            "crimson sheer tones",
            "mesh infernal hints"
        ],
        "colors": ["fiery red", "obsidian black", "sultry purple"]
    },
    "pirate_cove": {
        "dress": [
            "off-shoulder blouse skirt tie",
            "corset over striped sash",
            "vested velvet sides"
        ],
        "lingerie": [
            "lace bralette flair",
            "satin thong gems",
            "mesh top allure"
        ],
        "accessories": [
            "gold hoops ears",
            "coin belt strap",
            "tricorn hat tilt"
        ],
        "stockings": [
            "thigh-highs stripes",
            "lace garters knot",
            "sea-toned sheer flow"
        ],
        "colors": ["pirate black", "treasure red", "booty gold"]
    },
    "chinese_fantasy": {
        "dress": [
            "cheongsam silk allure modest",
            "hanfu mini sleeves",
            "qipao velvet openings"
        ],
        "lingerie": [
            "silk bralette petal",
            "lace thong ties",
            "satin slip light"
        ],
        "accessories": [
            "jade pendant cord",
            "tassel hairpin sway",
            "silk fan shield"
        ],
        "stockings": [
            "silk pattern weave",
            "red garters accent",
            "pearl-laced shine"
        ],
        "colors": ["imperial red", "dragon gold", "jade green"]
    },
    "japanese_onsen": {
        "dress": [
            "tied yukata print",
            "silk robe elegance",
            "cotton wrap tease modest"
        ],
        "lingerie": [
            "silk bralette hem",
            "lace thong knot",
            "mesh slip mist"
        ],
        "accessories": [
            "blossom hair clip",
            "necklace pendant drop",
            "geta sandals step"
        ],
        "stockings": [
            "thigh-highs rise",
            "tabi style tease",
            "lace garters hold"
        ],
        "colors": ["steam white", "cherry pink", "night indigo"]
    },
    "slavic_fantasy": {
        "dress": [
            "linen mini charm",
            "tunic collar open modest",
            "wool wrap allure"
        ],
        "lingerie": [
            "lace bralette bloom",
            "satin thong tease",
            "mesh slip edge"
        ],
        "accessories": [
            "flower crown ribbon",
            "beaded necklace layered",
            "woven belt charmed"
        ],
        "stockings": [
            "thigh-highs pattern",
            "cream lace veil",
            "garters cultural"
        ],
        "colors": ["snow white", "berry red", "forest green"]
    },
    "roman_gladiator": {
        "dress": [
            "tunic pleated flirt modest",
            "leather crop skirt",
            "linen drape arena"
        ],
        "lingerie": [
            "bralette hold",
            "lace thong edge",
            "satin slip smooth"
        ],
        "accessories": [
            "armband wrapping",
            "sandal straps climbing",
            "helmet plumed"
        ],
        "stockings": [
            "leather thigh-highs",
            "accented sheer bronze",
            "lace garters sand"
        ],
        "colors": ["arena bronze", "empire red", "colosseum black"]
    },
    "arcane_arena": {
        "dress": [
            "robe mini open front",
            "tunic cut deep",
            "combat gown slit"
        ],
        "lingerie": [
            "lace bralette rune",
            "satin thong trim silver",
            "bodysuit mesh glowing"
        ],
        "accessories": [
            "pendant glow hanging",
            "ring gemmed silver",
            "arm protector arcane"
        ],
        "stockings": [
            "thigh-highs lace rune",
            "garters sheer glow",
            "patterns silk arcane"
        ],
        "colors": ["void black", "magic gold", "battle scarlet"]
    },
    "shadow_realm": {
        "dress": [
            "black slip sleeves",
            "mini dress velvet shimmer",
            "gown silk flow glowing"
        ],
        "lingerie": [
            "bralette lace shadow",
            "satin thong silver",
            "slip mesh soft"
        ],
        "accessories": [
            "choker neck glow",
            "anklet silver charm",
            "accessory veil dark"
        ],
        "stockings": [
            "thigh-highs sheer dark",
            "garters lace shadow",
            "stockings mesh shimmer"
        ],
        "colors": ["abyss black", "twilight purple", "midnight blue"]
    },
    "enchanted_boudoir": {
        "dress": [
            "chemise silk laced neck low modest",
            "robe velvet tie loose",
            "gown lace short ruffled"
        ],
        "lingerie": [
            "bralette lace floral",
            "thong satin strapped",
            "slip mesh ribbon"
        ],
        "accessories": [
            "necklace pearl drape",
            "wrists lace cuffed",
            "hair ribbon enchanted"
        ],
        "stockings": [
            "tops silk laced",
            "garters sheer pastel",
            "thigh-high hold lace"
        ],
        "colors": ["blush pink", "soft ivory", "midnight black"]
    },
    "high_fantasy": {
        "dress": [
            "gown silk trim silver back open modest",
            "mini velvet off-shoulder",
            "tunic lace hem flowing"
        ],
        "lingerie": [
            "bralette lace elven",
            "thong satin gold",
            "slip mesh embroidered"
        ],
        "accessories": [
            "tiara golden light",
            "bracelet silver charmed",
            "brooch enchanted"
        ],
        "stockings": [
            "thigh-highs silk thread silver",
            "garters lace fantasy",
            "sheer glow faint"
        ],
        "colors": ["elf white", "realm gold", "sky blue"]
    },
    "mystical_brothel": {
        "dress": [
            "mini silk laced cut deep modest",
            "gown velvet plunging",
            "chiffon sheer shimmer"
        ],
        "lingerie": [
            "bralette lace jeweled",
            "thong satin ribbon",
            "slip mesh floral"
        ],
        "accessories": [
            "choker ruby hugging",
            "fan silk pearled",
            "ankle chain delicate"
        ],
        "stockings": [
            "thigh-high lace bowed",
            "garters sheer scarlet",
            "trim silk laced"
        ],
        "colors": ["lust scarlet", "velvet black", "seduce pink"]
    },
    "magical_academy": {
        "dress": [
            "skirt pleated blouse short modest",
            "robe open neck low",
            "tunic velvet rune mini"
        ],
        "lingerie": [
            "bralette lace rune",
            "thong satin glow",
            "slip mesh magical"
        ],
        "accessories": [
            "hairpin enchanted",
            "strap book pouch",
            "glow wand charm"
        ],
        "stockings": [
            "lace thigh-high rune",
            "garters sheer glow",
            "patterns silk academy"
        ],
        "colors": ["scholar black", "page white", "ink navy"]
    },
    "dieselpunk": {
        "dress": [
            "jacket leather cropped skirt",
            "dress utility brass",
            "mini velvet gear"
        ],
        "lingerie": [
            "bralette satin strapped",
            "thong lace metal",
            "slip mesh rivet"
        ],
        "accessories": [
            "goggles brass head",
            "belt leather",
            "bracelet copper"
        ],
        "stockings": [
            "thigh-highs garter leather",
            "tones sheer rust",
            "accents lace brass"
        ],
        "colors": ["engine black", "steel gray", "fuel rust"]
    },
    "cyberpunk_redlight": {
        "dress": [
            "jacket crop neon skirt",
            "bodysuit holo cutout",
            "mini silk digital"
        ],
        "lingerie": [
            "bralette lace neon",
            "thong satin LED",
            "slip mesh holo"
        ],
        "accessories": [
            "choker neon",
            "arm cuff cyber",
            "earring glowing"
        ],
        "stockings": [
            "lace thigh-high neon",
            "garters sheer glow",
            "patterns lace cyber"
        ],
        "colors": ["neon pink", "electric blue", "shadow black"]
    },
    "forbidden_temple": {
        "dress": [
            "robe silk slit modest",
            "linen embroidery gold",
            "gown velvet rune"
        ],
        "lingerie": [
            "bralette lace sigil",
            "thong satin laced",
            "slip mesh glow"
        ],
        "accessories": [
            "amulet gold",
            "bracelet wooden",
            "pendant carved"
        ],
        "stockings": [
            "lace thigh-high rune",
            "garters sheer gold",
            "patterns silk temple"
        ],
        "colors": ["secret black", "idol gold", "ritual scarlet"]
    },
    "victorian_steampunk": {
        "dress": [
            "dress short corset laced",
            "mini velvet copper",
            "blouse skirt silk brass"
        ],
        "lingerie": [
            "bralette lace gear",
            "thong satin overlay",
            "slip mesh copper"
        ],
        "accessories": [
            "pendant watch pocket",
            "gloves lace",
            "choker brass"
        ],
        "stockings": [
            "lace thigh-high gear",
            "garters sheer copper",
            "lace silk Victorian"
        ],
        "colors": ["wine burgundy", "gear black", "steam copper"]
    },
    "sexual_teacher": {
        "dress": [
            "blouse skirt pencil unbuttoned modest",
            "dress short deep modest",
            "dress blazer mini"
        ],
        "lingerie": [
            "bralette lace strapped",
            "thong satin edged",
            "slip mesh trim"
        ],
        "accessories": [
            "glasses reading",
            "ruler silver pendant",
            "book strap leather"
        ],
        "stockings": [
            "tops thigh-high laced",
            "garters sheer black",
            "patterns silk subtle"
        ],
        "colors": ["strict black", "pure white", "forbidden red"]
    },
    "maid_fantasy": {
        "dress": [
            "maid short frilly",
            "dress apron open neck modest",
            "uniform mini lace trimmed"
        ],
        "lingerie": [
            "camisole lace bowed",
            "thong satin ruffled",
            "bralette mesh ribbon"
        ],
        "accessories": [
            "choker lace",
            "headband maid",
            "duster feather charm"
        ],
        "stockings": [
            "thigh-high bowed",
            "garters sheer lace",
            "silk frilled"
        ],
        "colors": ["innocent white", "service black", "playful pink"]
    },
    "urban_fantasy_office": {
        "dress": [
            "skirt blazer mini fit",
            "dress office sleeve sheer modest",
            "dress jacket cropped short"
        ],
        "lingerie": [
            "bralette lace strapped",
            "thong satin trim",
            "slip mesh form"
        ],
        "accessories": [
            "necklace ID silver",
            "wrist watch leather",
            "earrings clip-on"
        ],
        "stockings": [
            "thigh-high sheer",
            "garters lace gray",
            "vibe silk office"
        ],
        "colors": ["corporate gray", "power black", "accent red"]
    },
    "ancient_egyptian": {
        "dress": [
            "linen short belted gold",
            "trim silk ankh",
            "tunic draped slit modest"
        ],
        "lingerie": [
            "bralette satin gold",
            "thong lace beaded",
            "slip mesh hieroglyph"
        ],
        "accessories": [
            "collar gold",
            "anklet ankh",
            "armband beaded"
        ],
        "stockings": [
            "silk sheer thread gold",
            "garters lace blue",
            "wraps thigh-high linen"
        ],
        "colors": ["Nile white", "pharaoh gold", "scarab blue"]
    },
    "celtic_druid": {
        "dress": [
            "mini linen embroidery leaf",
            "tunic wool low modest",
            "wrap silk vine"
        ],
        "lingerie": [
            "bralette lace vine",
            "thong satin green",
            "slip mesh floral"
        ],
        "accessories": [
            "crown leaf",
            "bead necklace wood",
            "bracelet woven"
        ],
        "stockings": [
            "lace thigh-high leaf",
            "garters sheer green",
            "motifs silk druid"
        ],
        "colors": ["earth green", "oak brown", "sun gold"]
    },
    "aztec_pyramid": {
        "dress": [
            "trim feather short",
            "wrap linen jade",
            "tunic silk gold"
        ],
        "lingerie": [
            "bralette satin beaded",
            "thong lace feathered",
            "slip mesh stone"
        ],
        "accessories": [
            "necklace jade",
            "bracelet feather",
            "anklet gold"
        ],
        "stockings": [
            "lace thigh-high beaded",
            "garters sheer red",
            "patterns silk Aztec"
        ],
        "colors": ["temple gold", "blood red", "jungle green"]
    },
    "samurai_dojo": {
        "dress": [
            "kimono short sash",
            "yukata mini",
            "tunic wrap silk tied"
        ],
        "lingerie": [
            "bralette silk bow",
            "thong lace tied",
            "slip mesh floral"
        ],
        "accessories": [
            "hairpin bamboo",
            "fan silk",
            "charm obi"
        ],
        "stockings": [
            "thigh-high silk",
            "garters sheer black",
            "patterns lace dojo"
        ],
        "colors": ["honor red", "shadow black", "purity white"]
    },
    "cowboy_saloon": {
        "dress": [
            "mini denim fringed vest",
            "short checkered belted",
            "tunic leather slit modest"
        ],
        "lingerie": [
            "bralette lace fringe",
            "thong satin embroidered",
            "slip mesh cowboy"
        ],
        "accessories": [
            "hat cowboy",
            "bracelet leather",
            "anklet spur"
        ],
        "stockings": [
            "thigh-high fringe",
            "garters sheer brown",
            "vibes lace saloon"
        ],
        "colors": ["dust brown", "sunset red", "night black"]
    },
    "horror_mansion": {
        "dress": [
            "slip black laced",
            "dress velvet tattered",
            "gown sheer cobweb"
        ],
        "lingerie": [
            "camisole lace cobweb",
            "thong satin laced",
            "bralette mesh dark"
        ],
        "accessories": [
            "necklace cross",
            "veil lace",
            "locket silver"
        ],
        "stockings": [
            "lace thigh-high torn",
            "garters sheer red",
            "motifs mesh horror"
        ],
        "colors": ["ghost black", "blood red", "fog gray"]
    },
    "fairy_tale_castle": {
        "dress": [
            "gown silk short floral",
            "dress velvet laced sleeves",
            "mini chiffon ruffled"
        ],
        "lingerie": [
            "bralette lace flower",
            "thong satin ribbon",
            "slip mesh petal"
        ],
        "accessories": [
            "tiara small",
            "pendant crystal",
            "choker ribbon"
        ],
        "stockings": [
            "thigh-high silk bowed",
            "garters sheer lace",
            "patterns lace fairy"
        ],
        "colors": ["enchant pink", "crown gold", "tale white"]
    },
    "volcanic_forge": {
        "dress": [
            "tunic leather mini",
            "top skirt crop ember",
            "wrap silk flame"
        ],
        "lingerie": [
            "bralette satin rivet",
            "thong lace flame",
            "slip mesh soot"
        ],
        "accessories": [
            "goggles",
            "belt tool leather",
            "pendant brass"
        ],
        "stockings": [
            "thigh-high leather",
            "garters sheer orange",
            "motifs lace forge"
        ],
        "colors": ["lava red", "ash black", "spark orange"]
    },
    "ice_palace": {
        "dress": [
            "slip trim fur",
            "mini velvet frost",
            "gown lace silk icy"
        ],
        "lingerie": [
            "bralette lace icicle",
            "thong satin snowflake",
            "slip mesh frost"
        ],
        "accessories": [
            "pendant frosted",
            "cuff silver",
            "crown charm ice"
        ],
        "stockings": [
            "lace silk thigh-high frost",
            "garters sheer blue",
            "patterns lace palace"
        ],
        "colors": ["frost white", "glacier blue", "ice silver"]
    },
    "desert_nomad": {
        "dress": [
            "short flowing scarf",
            "skirt mini crop linen",
            "tunic wrap silk slit modest"
        ],
        "lingerie": [
            "bralette coin",
            "thong lace veil",
            "slip mesh bead"
        ],
        "accessories": [
            "anklet gold",
            "head scarf woven",
            "chain belly"
        ],
        "stockings": [
            "thigh-high sheer thread gold",
            "garters lace red",
            "patterns silk nomad"
        ],
        "colors": ["dune gold", "spice red", "sand brown"]
    },
    "medieval_tavern": {
        "dress": [
            "skirt blouse short corset",
            "dress loose off-shoulder modest",
            "tunic linen low belted"
        ],
        "lingerie": [
            "bralette lace ribbon",
            "thong satin trim",
            "slip mesh frill"
        ],
        "accessories": [
            "belt pouch",
            "pendant wooden",
            "choker leather"
        ],
        "stockings": [
            "thigh-high wool laced",
            "garters sheer cream",
            "motifs lace tavern"
        ],
        "colors": ["ale brown", "fire red", "linen cream"]
    },
    "renaissance_court": {
        "dress": [
            "gown brocade short",
            "neckline silk low modest",
            "tunic velvet laced"
        ],
        "lingerie": [
            "bralette lace pearl",
            "thong satin laced",
            "slip mesh gold"
        ],
        "accessories": [
            "necklace pearl",
            "mask feathered",
            "fan silk"
        ],
        "stockings": [
            "lace thigh-high ribbon",
            "garters sheer crimson",
            "patterns silk court"
        ],
        "colors": ["royal gold", "court crimson", "elegant ivory"]
    },
    "industrial_revolution": {
        "dress": [
            "buttons linen brass",
            "skirt mini leather crop",
            "tunic embroidery velvet gear"
        ],
        "lingerie": [
            "bralette gear motif",
            "thong lace trim",
            "slip mesh rivet"
        ],
        "accessories": [
            "pendant brass",
            "gloves lace",
            "choker leather"
        ],
        "stockings": [
            "lace thigh-high gear",
            "garters sheer brown",
            "patterns silk industrial"
        ],
        "colors": ["smoke gray", "factory brown", "gear black"]
    },
    "underwater_kingdom": {
        "dress": [
            "slip trim pearl flowing",
            "mini sheer aqua seashell",
            "gown wrap silk wave"
        ],
        "lingerie": [
            "bralette lace strap pearl",
            "thong silk charm seashell",
            "slip mesh bubble"
        ],
        "accessories": [
            "necklace pearl",
            "hairpin coral",
            "bracelet shell"
        ],
        "stockings": [
            "thigh-high sheer pearl",
            "garters lace turquoise",
            "motifs silk underwater"
        ],
        "colors": ["ocean aqua", "shell pearl white", "wave turquoise"]
    },
    "mushroom_forest": {
        "dress": [
            "short embroidery linen mushroom",
            "tunic sheer mini leafy",
            "gown velvet fungal"
        ],
        "lingerie": [
            "bralette lace floral",
            "thong satin nature",
            "slip mesh spore"
        ],
        "accessories": [
            "pendant necklace mushroom",
            "bracelet woven vine",
            "headpiece leaf"
        ],
        "stockings": [
            "lace thigh-high mushroom",
            "garters sheer green",
            "patterns silk forest"
        ],
        "colors": ["moss green", "earth brown", "spore cream"]
    },
    "desert_oasis": {
        "dress": [
            "wrap flow linen slit high modest",
            "trim silk short golden",
            "tunic side chiffon opening"
        ],
        "lingerie": [
            "bralette satin coin",
            "thong lace panel sheer",
            "slip mesh bead"
        ],
        "accessories": [
            "anklet gold",
            "head scarf woven",
            "charm necklace oasis"
        ],
        "stockings": [
            "thigh-high sheer gold",
            "garters lace sand",
            "patterns silk oasis"
        ],
        "colors": ["mirage gold", "palm sand", "pool turquoise"]
    },
    "bamboo_forest": {
        "dress": [
            "yukata short pattern bamboo",
            "wrap silk green trim",
            "tunic linen accents leafy"
        ],
        "lingerie": [
            "bralette lace edge floral",
            "thong silk ribbon",
            "slip mesh bamboo"
        ],
        "accessories": [
            "hairpin bamboo",
            "bracelet jade",
            "pendant leaf"
        ],
        "stockings": [
            "thigh-high silk laced",
            "garters sheer green",
            "patterns lace forest"
        ],
        "colors": ["bamboo green", "mist white", "stalk brown"]
    },
    "northern_lights": {
        "dress": [
            "mini aurora shimmer",
            "slip belt trim fur silver",
            "tunic hems velvet glow"
        ],
        "lingerie": [
            "bralette lace icy",
            "thong satin aurora",
            "slip mesh light"
        ],
        "accessories": [
            "necklace crystal snowflake",
            "cuff silver arm",
            "headpiece glowing"
        ],
        "stockings": [
            "thigh-high sheer shimmer",
            "garters lace purple",
            "patterns silk light"
        ],
        "colors": ["aurora blue", "night purple", "snow white"]
    },
}

STAGE_CONFIG = {
    'presentation': {
        'type': 'stage',
        'poses': [
            '1girl, full body, standing straight, hands behind back, chest forward, confident smile, elegant posture',
            '1girl, leaning gracefully against a wall, one leg crossed, playful glance, hair cascading over shoulder',
            '1girl, walking slowly, dress flowing in motion, looking back over shoulder, cinematic elegance',
            '1girl, sitting elegantly on ornate chair, legs crossed, hands on knees, soft gentle smile',
            '1girl, spinning gracefully, hair and dress flowing, joyful radiant expression',
            '1girl, bending forward slightly, hands clasped, cute playful smile, natural charm',
            '1girl, arms outstretched, welcoming gesture, bright radiant smile, glowing presence'
        ],
        'view_angles': [
            'full body view, elegant silhouette, complete figure visible',
            'low angle, legs elongated, emphasizing power and grace',
            'side profile, subtle curves highlighted by soft lighting',
            'three-quarter view, natural cinematic framing',
            'eye-level portrait, direct emotional connection with viewer',
            'slightly above, graceful feminine silhouette in focus',
            'dynamic tilted angle, movement and flow captured'
        ],
        'emotion': [
            'confident radiance',
            'playful charm',
            'graceful poise',
            'charming allure',
            'joyful glow',
            'seductive smile',
            'looking directly at viewer with intensity'
        ],
        'clothing_logic': 'full_dressed',
        'variations': NUM_VARIATIONS,
        'extra_prompts': [
            'masterpiece, best quality, elegant composition, photogenic beauty',
            'soft cinematic lighting, warm highlights, smooth shading',
            'graceful movement, feminine charm, intricate detail',
            'delicate fabrics, flowing motion, timeless elegance'
        ],
        'negative_prompt': 'awkward pose, ugly expression, bad anatomy, unflattering lighting, stiff posture'
    },

    'victory': {
        'type': 'stage',
        'poses': [
            '1girl, leaping joyfully into the air, arms raised, glowing triumphant smile',
            '1girl, standing tall, chest forward, one arm raised high glowing with magical energy, radiant victorious smile',
            '1girl, spinning with arms wide, magical sparkles surrounding her body, confident dazzling look'
        ],
        'view_angles': [
            'low angle, dramatic perspective, emphasizing height and victory',
            'eye-level close-up, glowing face and magical aura in focus',
            'three-quarter view, flowing body movement, energy radiating'
        ],
        'emotion': [
            'happy triumph',
            'joyful celebration',
            'proud confidence',
            'excited glow',
            'victorious energy'
        ],
        'clothing_logic': 'full_dressed',
        'variations': NUM_VARIATIONS,
        'extra_prompts': [
            'masterpiece, glowing aura, magical sparks, cinematic glow',
            'dynamic energy, radiant movement, celebration moment',
            'epic composition, triumphant expression, high detail'
        ],
        'negative_prompt': 'sadness, defeat, fatigue, boredom, dull energy, crying, losing, lifeless pose'
    },

    'defeat': {
        'type': 'stage',
        'poses': [
            '1girl, collapsed on floor, sitting with legs folded loosely, head bowed, arms resting on thighs, exhausted expression',
            '1girl, fallen back, knees bent, one arm supporting body weakly, eyes lowered in despair',
            '1girl, kneeling on ground, body slouched, arms hanging limply, hair covering face, defeated posture'
        ],
        'view_angles': [
            'high overhead angle, subject small and vulnerable in frame',
            'ground-level close-up, intimate defeated look, eyes half-closed',
            'diagonal tilted framing, imbalance and weakness captured'
        ],
        'emotion': [
            'exhausted sorrow',
            'vulnerable despair',
            'reluctant acceptance',
            'helplessness',
            'quiet suffering'
        ],
        'clothing_logic': 'torn',
        'variations': NUM_VARIATIONS,
        'extra_prompts': [
            'dim magical afterglow, faint fading aura',
            'cinematic shadows, broken posture, soft highlights',
            'desaturated tones, atmosphere of loss'
        ],
        'negative_prompt': 'confident, victorious, empowered, sexual excitement, triumphant energy, cum'
    },
    # 'demonstration_legs': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, seated with legs crossed, heel dangling, skirt lifted, sly smile',
    #         '1girl, reclining on chair, leg extended forward, hand brushing thigh, seductive gaze',
    #         '1girl, standing with leg raised on stool, skirt sliding up, leaning forward, teasing look',
    #         '1girl, lying on bed, legs slightly parted, feet pointed, inviting glance',
    #         '1girl, sitting on edge, legs stretched out, hands resting on thighs, confident smile'
    #     ],
    #     'view_angles': [
    #         'low angle, focus on legs and thighs, smooth lines',
    #         'side view, leg extended, elegant curve',
    #         'angled view, crossed legs, stockings visible',
    #         'close-up on legs and feet, delicate details',
    #         'three-quarter view, full leg length emphasized'
    #     ],
    #     'clothing_logic': 'full_dressed',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['teasing smile, confident gaze, inviting expression, looking at viewer'],
    #     'extra_prompts': [
    #         'beautiful legs, smooth skin, elegant curves',
    #         'sexy stockings, delicate footwear',
    #         'legs focus, feminine grace, sensual'
    #     ],
    #     'negative_prompt': 'naked, nude, poor leg anatomy, short legs, muscular legs'
    # },
    # 'demonstration_breasts': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, hands cupping breasts from below, leaning forward, teasing smile',
    #         '1girl, hands pressing under breasts, pushing upward, playful grin',
    #         '1girl, hands holding breasts together, arching back, flirty gaze',
    #         '1girl, hands covering breasts, cleavage visible, coy expression',
    #         '1girl, arms squeezing breasts together, leaning forward, mischievous glance',
    #         '1girl, hands holding breasts, blushing, half-smile'
    #     ],
    #     'view_angles': [
    #         'low angle, focus on hands lifting breasts, neckline emphasized',
    #         'close-up, breasts cupped by hands, skin detail',
    #         'diagonal view, hands pressing breasts together',
    #         'eye-level, gaze at viewer while holding breasts',
    #         'side angle, hand lifting breast, softness detail'
    #     ],
    #     'clothing_logic': 'full_dressed',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['teasing smile, playful seduction, coy blush, looking at viewer'],
    #     'extra_prompts': [
    #         'fabric strain, tight top, curves emphasized',
    #         'cleavage tease, partially revealed',
    #         'erotic presentation, seductive'
    #     ],
    #     'negative_prompt': 'cum, cum on breasts'
    # },
    # 'demonstration_ass': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, standing, rear view, perfect ass, hands on ass, bent over, looking back',
    #         '1girl, kneeling, rear view, perfect ass, arching back, hands spreading ass, glancing back',
    #         '1girl, on all fours, rear view, perfect ass, presenting hips, seductive confidence',
    #         '1girl, leaning against wall, rear view, perfect ass, hips pushed back, sly grin'
    #     ],
    #     'view_angles': [
    #         'rear view, focus on hips and ass curve',
    #         'low angle from behind, emphasizing ass and thighs',
    #         'over the shoulder view, ass in frame',
    #         'diagonal rear angle, hip curve and roundness',
    #         'close-up crop on ass and hips, skin texture'
    #     ],
    #     'clothing_logic': 'full_dressed',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['sly grin, seductive confidence, looking back at viewer'],
    #     'extra_prompts': [
    #         'curve focus, perfect arch, hips emphasized'
    #     ],
    #     'negative_prompt': 'frontal view, side view, clothed ass, cropped body',
    # },
    # 'demonstration_ass_doggy': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, sexy pose, eyes half open, on all fours:1.6, head on ground, knees together, feet apart, bulging ass',
    #     ],
    #     'view_angles': [
    #         'high angle shot, view from behind, emphasizing ass and thighs',
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['smile expression'],
    #     'extra_prompts': [
    #         'curve focus'
    #     ],
    #     'negative_prompt': 'frontal view, side view, clothed ass, cropped body',
    # },
    # 'demonstration_ass_doggy_sideview': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, sexy pose, eyes half open, on all fours:1.6, head on ground:1.5, '
    #         'elbows on the ground:1.4, looking at viewer, bulging ass',
    #     ],
    #     'view_angles': [
    #         'perpendicular side view:1.6, focus on the curve of the back and ass',
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['languid gaze'],
    #     'extra_prompts': [
    #         'curve focus, perfect arch, hips emphasized'
    #     ],
    #     'negative_prompt': ' frontal view, back view, clothed ass, cropped body',
    # },
    # 'demonstration_panties_show': {
    #     'type': 'stage',
    #     'poses': [
    #         '(skirt lift tease:1.6), 1girl, lifting dress hem with both hands, revealing panties, playful smile',
    #         '(over-shoulder reveal:1.5), 1girl, bending forward, looking back, holding skirt up, cheeky expression',
    #         '(side peek:1.4), 1girl, standing sideways, lifting dress to show panties profile, seductive glance',
    #         '(chair reveal:1.5), 1girl, sitting on edge, legs crossed, lifting skirt slowly, knowing look'
    #     ],
    #     'view_angles': [
    #         '(low angle reveal:1.6), from below focusing on panties and upper thighs',
    #         '(intimate close-up:1.7), tight shot on panties area, fabric details visible',
    #         '(three-quarter view:1.5), showing both body curve and the reveal',
    #         '(from behind:1.4), rear angle with skirt lifted, emphasizing curves',
    #         '(diagonal perspective:1.5), dynamic angle capturing the teasing moment'
    #     ],
    #     'clothing_logic': 'full_dressed',  # Одежда на месте, просто приподнята
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'extra_prompts': [
    #         '(fabric tension:1.4), skirt held taut, revealing shape underneath',
    #         '(teasing reveal:1.5), partial exposure, leaving something to imagination',
    #         '(elegant lingerie:1.3), delicate panties, decorative details visible'
    #     ],
    #     'negative_prompt': 'completely naked, fully exposed, no panties, completely covered'
    # },
    # 'demonstration_underboob': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, arms lifted overhead, shirt riding up, underboob visible, playful smile',
    #         '1girl, stretching back, crop top sliding up, underboob tease, seductive glance',
    #         '1girl, leaning sideways, tank top loose, underboob exposure, coy grin'
    #     ],
    #     'view_angles': [
    #         'low angle, focus on chest and underboob',
    #         'three-quarter view, body curves emphasized',
    #         'close-up crop on underboob, fabric strain'
    #     ],
    #     'clothing_logic': 'full_dressed',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['teasing, confident, playful, seductive, looking at viewer'],
    #     'extra_prompts': [
    #         '(fabric strain:1.4), shirt pulled up by arms',
    #         'tight top sliding, skin reveal',
    #         'underboob focus, delicate highlight'
    #     ],
    #     'negative_prompt': 'fully topless, no fabric, no clothing'
    # },
    # 'bedroom_intimacy': {
    #     'type': 'stage',
    #     'poses': [
    #         '1girl, lying on bed, arching back, lingerie slipping off shoulders, inviting smile',
    #         '1girl, kneeling on bed, leaning forward, cleavage exposed, mischievous glance',
    #         '1girl, lying sideways, sheet loosely draped, bare thighs, coy expression'
    #     ],
    #     'view_angles': [
    #         'close-up chest framed by sheets',
    #         'from above, intimate bed pose',
    #         'angled side shot, lingerie slipping'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'variations': NUM_VARIATIONS,
    #     'emotion': ['seductive, inviting, playful, sultry'],
    #     'extra_prompts': [
    #         'soft bed sheets, warm lighting',
    #         'lingerie slipping, curves emphasized',
    #         'romantic atmosphere, intimate setting'
    #     ],
    #     'negative_prompt': 'full nudity, no clothing, messy background'
    # },
    # 'submissive_pose': {
    #     'type': 'stage',
    #     'poses': [
    #         '(on all fours:1.5), 1girl, head pressed to floor, hips raised high, arms stretched forward, submissive posture',
    #         '(arch back:1.4), 1girl, on hands and knees, back arched, chest close to ground, strict side profile',
    #         '(low bow:1.5), 1girl, kneeling on all fours, forehead touching floor, ass elevated, vulnerable display'
    #     ],
    #     'view_angles': [
    #         '(strict side view:1.6), full profile body alignment',
    #         '(ground-level side:1.5), intimate horizontal framing',
    #         '(close-up hip focus:1.4), cropped body detail from side'
    #     ],
    #     'clothing_logic': 'full_naked',  # или "nude", если нужно смелее
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy glance upward, eyes toward viewer',
    #         'nervous blush, submissive expression',
    #         'vulnerable but seductive eye contact'
    #     ],
    #     'extra_prompts': [
    #         'arched back silhouette, ass elevated',
    #         'strict profile framing, clean composition',
    #         'focus on body curve, elegant tension'
    #     ],
    #     'negative_prompt': 'rear view, frontal view, diagonal angle, standing pose'
    # },
    # 'titsjob': {
    #     'type': 'action',
    #     'poses': [
    #         'breasts together, 1girl, pov from above, grabbing own breasts, paizuri, penis between breasts, titjob, small penis:1.9, squatting down and leaning forward, dinamic angle, looking at penis BREAK (1boy, standing)',
    #         'breasts together, 1girl, grabbing own breasts, paizuri, pov from above, penis between breasts, titjob, small penis:1.9, squatting down and leaning forward, dinamic angle, looking at penis BREAK (1boy, standing)'
    #     ],
    #     'view_angles': [
    #         '(close bust:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors',
    #         '(close bust:1.4), intimate effect, brush strokes visible, artistic interpretation'
    #     ],
    #     'clothing_logic': 'full_naked',  # Одежда на месте, просто приподнята
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'negative_prompt': '((bra)):1.6, multiple people:1.9, crowd, extra figures, additional characters:1.9, cum, cumshot, cum on face, cum on chest',
    #     'extra_prompts': []
    # },
    # 'titsjob_cum_on_face': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, on all fours, perfect shape ass, dinamic angle, POV, underface, underboob, cum on face:1.2, cum on hair, penis on face, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes',
    #         'pov, 1girl, 1boy, POV, on all fours, perfect shape ass, dinamic angle, looking at viewer, underface, underboob, cum on face:1.2, cum on hair, penis on face, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes, pov crotch, pov penis'
    #     ],
    #     'view_angles': [
    #         '(extreme close-up:1.6), intimate bust focus, cleavage emphasis, skin texture visible, shallow depth of field',
    #         '(close bust:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '((bra)):1.6, cum on chest, cum on breasts, cum on ass, blowjob, titjob, paizuri, handjob, penis in mouth, cum in ass, cum over ass, cum around ass, multiple people:1.9, crowd, extra figures, additional characters:1.9',
    #     'extra_prompts': []
    # },
    # 'titsjob_cum_on_tits': {
    #     'type': 'action',
    #     'poses': [
    #         'massive cumshot, cum on chest, cum on breasts, POV, 1girl, 1boy, grabbing own breasts, pov from above, looking up to viewer, pov crotch, pov penis, middle penis, squatting down and leaning forward, surprise',
    #         'massive cumshot, cum on chest, cum on breasts, 1girl, 1boy, POV, grabbing own breasts, middle penis, squatting down and leaning forward, surprise'
    #     ],
    #     'view_angles': [
    #         '(close bust:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors',
    #         '(close frontal intimacy:1.5), direct upper body view, eye contact maintained',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '((bra)):1.6, multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, cum on face, blowjob, titjob, paizuri, handjob, penis in mouth',
    #     'extra_prompts': []
    # },
    # 'titsjob_cum_in_mouth': {
    #     'type': 'action',
    #     'poses': [
    #         'short penis, wide open mouth, leaning forward, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, grabbing own breasts, cumshot, POV, overloaded cum, huge cumshot, rolling eyes, еcstasy, full mouth of cum, penis in mouth',
    #         'short penis, wide open mouth, leaning forward, pov, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, grabbing own breasts, pov from above, cumshot, POV, huge cumshot, rolling eyes, еcstasy, full mouth of cum, penis in mouth'
    #     ],
    #     'view_angles': [
    #         '(close face:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors',
    #         '(extreme proximity:1.6), intimate closeness, barely any background, focused on skin and texture'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '((bra)):1.6, multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, cum on face, blowjob, titjob, paizuri, handjob, penis in mouth',
    #     'extra_prompts': []
    # },
    # 'handjob': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy standing, dinamic angle, fear, submissive, POV, handjob, middle penis:1.9, leaning forward',
    #         'pov, 1girl, 1boy standing, handjob, pov from above, middle penis:1.9, leaning forward, dinamic angle, looking at viewer, fear, submissive'
    #     ],
    #     'view_angles': [
    #         '(dynamic motion blur:1.4), intimate movement capture, slight motion blur, sensual energy',
    #         '(close bust:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on chest, cum on breasts, cum on ass, blowjob, titjob, paizuri, cum in ass, cum over ass, cum around ass',
    #     'extra_prompts': []
    # },
    # 'handjob_cum_on_face': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, on all fours, perfect shape ass, dinamic angle, POV, underface, underboob, cum on face:1.6, cum on hair, penis on face, handjob, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes, suddenly',
    #         'pov, 1girl, 1boy, pov from above, on all fours, perfect shape ass, dinamic angle, looking at viewer, underface, underboob, cum on face:1.2, cum on hair, penis on face, handjob, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes, pov crotch, pov penis, suddenly'
    #     ],
    #     'view_angles': [
    #         '(intimate over-shoulder:1.4), view from behind emphasizing back and shoulder blades',
    #         '(close frontal intimacy:1.5), direct upper body view, eye contact maintained',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on chest, cum on breasts, cum on ass, blowjob, titjob, paizuri, penis in mouth, cum in ass, cum over ass, cum around ass, multiple people:1.9, crowd, extra figures, additional characters:1.9',
    #     'extra_prompts': []
    # },
    # 'handjob_cum_on_tits': {
    #     'type': 'action',
    #     'poses': [
    #         'middle penis, cum on chest, cum on breasts, squatting down and leaning forward, 1girl, 1boy, overflow:1.5, cum bubbling, cumshot,  huge cumshot, rolling eyes, POV, еcstasy, handjob, breasts in profile view',
    #         'middle penis, cum on chest, cum on breasts, squatting down and leaning forward, pov, 1girl, 1boy, overflow:1.5, cum bubbling, pov from above, cumshot,  huge cumshot, rolling eyes, еcstasy, handjob, breasts in profile view'
    #     ],
    #     'view_angles': [
    #         '(close bust:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors',
    #         '(upper body focus:1.3), intimate framing from chest to head, warm lighting',
    #         '(intimate three-quarter:1.4), 45-degree angle highlighting shoulders and neck'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '((bra)):1.6, multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, cum on face, blowjob, titjob, paizuri, penis in mouth',
    #     'extra_prompts': []
    # },
    # 'handjob_cum_in_mouth': {
    #     'type': 'action',
    #     'poses': [
    #         'middle penis, wide open mouth, squatting down and leaning forward, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, cumshot,  huge cumshot, rolling eyes, POV, еcstasy, full mouth of cum, penis in mouth, handjob, blowjob, deepthroat',
    #         'middle penis, wide open mouth, squatting down and leaning forward, pov, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, pov from above, cumshot,  huge cumshot, rolling eyes, еcstasy, full mouth of cum, penis in mouth, handjob, blowjob, deepthroat'
    #     ],
    #     'view_angles': [
    #         '(intimate over-shoulder:1.4), view from behind emphasizing back and shoulder blades',
    #         '(close frontal intimacy:1.5), direct upper body view, eye contact maintained',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, titjob, paizuri',
    #     'extra_prompts': []
    # },
    # 'blowjob': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, POV, blowjob, middle penis:1.9, on all fours, perfect shape ass, wide opened eyes, dinamic angle, looking at viewer, submissive, deepthroat, surprised, petting head',
    #         'pov, 1girl, 1boy, blowjob, pov from above, middle penis:1.9, on all fours, perfect shape ass, wide opened eyes, dinamic angle, looking at viewer, submissive, deepthroat, surprised, petting head'
    #     ],
    #     'view_angles': [
    #         '(intimate Dutch angle:1.3), tilted composition creating dynamic upper body focus',
    #         '(soft top-down:1.4), gentle overhead angle emphasizing décolletage',
    #         '(intimate quarter-turn:1.3), slight body turn highlighting bust contour'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, titjob, paizuri',
    #     'extra_prompts': []
    # },
    # 'blowjob_cum_on_face': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, on all fours, perfect shape ass, dinamic angle, POV, looking at viewer, underface, underboob, cum on face:1.2, cum on hair, penis on face, handjob, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes, suddenly',
    #         'pov, 1girl, 1boy, pov from above, on all fours, perfect shape ass, dinamic angle, looking at viewer, underface, underboob, cum on face:1.2, cum on hair, penis on face, handjob, cumshot, projectile cum, wide angle, (midshot, sexy pose:1.3), closed eyes, pov crotch, pov penis, suddenly'
    #     ],
    #     'view_angles': [
    #         '(close face:1.4), intimate ecchi perspective, exaggerated proportions, vibrant colors',
    #         '(close frontal intimacy:1.5), direct upper body view, eye contact maintained',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on chest, cum on breasts, cum on ass, blowjob, titjob, paizuri, penis in mouth, cum in ass, cum over ass, cum around ass, multiple people:1.9, crowd, extra figures, additional characters:1.9',
    #     'extra_prompts': []
    # },
    # 'blowjob_cum_on_tits': {
    #     'type': 'action',
    #     'poses': [
    #         'massive cumshot, cum on chest, cum on breasts, 1girl, 1boy, pov from above, looking at breasts, middle penis, squatting down and leaning forward, surprise, after blowjob, wide opened mouth, smile, head is lowered',
    #         'massive cumshot, cum on chest, cum on breasts, 1girl, 1boy, pov from above, looking at own breasts, pov crotch, pov penis, middle penis, POV, squatting down and leaning forward, surprise, after blowjob, wide opened mouth, smile, head is lowered'
    #     ],
    #     'view_angles': [
    #         '(intimate close-up:1.5), face and décolletage focus, soft lighting, tender expression',
    #         '(dramatic close-up:1.5), face and chest focus, chiaroscuro lighting',
    #         '(close bust:1.4), intimate blowjob perspective, vibrant colors'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '((bra)):1.6, multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, cum on face, titjob, paizuri, penis in mouth',
    #     'extra_prompts': []
    # },
    # 'blowjob_cum_in_mouth': {
    #     'type': 'action',
    #     'poses': [
    #         'short penis, wide open mouth, squatting down and leaning forward, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, cumshot, POV, huge cumshot, rolling eyes, еcstasy, full mouth of cum, penis in mouth, handjob, blowjob, deepthroat, tongue stuck out',
    #         'short penis, wide open mouth, squatting down and leaning forward, pov, 1girl, 1boy, cum in mouth:1.5, overflow:1.5, cum bubbling, pov from above, cumshot, huge cumshot, rolling eyes, еcstasy, full mouth of cum, penis in mouth, handjob, blowjob, deepthroat, tongue stuck out'
    #     ],
    #     'view_angles': [
    #         '(intimate embrace focus:1.5), upper body in arms, faces close together',
    #         '(whispering proximity:1.4), intimate distance emphasizing lips and neck',
    #         '(intimate chiaroscuro:1.5), dramatic lighting on upper body, deep shadows',
    #         '(soft focus intimacy:1.4), dreamy atmosphere, sharp upper body details'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'multiple people:1.9, crowd, extra figures, additional characters:1.9, cum on ass, titjob, paizuri',
    #     'extra_prompts': []
    # },
    # 'foursome_doggy_cum_on_body': {
    #     'type': 'action',
    #     'poses': [
    #         '3girls, feet, toes, from_behind, side-by-side, pov, foursome, from above, testicles, ((1man, man out of frame)), (on all fours, perfect shape asses):1.9, ass grab, buttjob, small anus, presenting ass, cum on ass:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectile cum)), first girl smile, second girl close eyes and open mouth, (first girl cum on hair and back):1.2, (second girl cum on back and ass):1.2, third girl cum on back and ass, first girl grab own ass, third girl grab own breasts',
    #         '3girls, feet, toes, from_behind, side-by-side, pov, foursome, from above, testicles, ((1man, man out of frame)), (on all fours, perfect shape asses):1.9, ass grab, buttjob, small anus, presenting ass, cum on ass:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectile cum)), first girl smile, second girl close eyes and open mouth, (first girl cum on hair and back):1.2, (second girl cum on back and ass):1.2, third girl cum on back and ass, first girl grab own ass, third girl grab own breasts'
    #     ],
    #     'view_angles': [
    #         '(extreme close-up:1.7), intimate focus on lower back and hip connection, skin texture detailed',
    #         '(motion capture:1.6), dynamic movement suggestion, hair flowing, energy and rhythm emphasis',
    #         '(close face:1.4), exaggerated proportions, vibrant colors'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'titjob, paizuri, multiple penis, identity censor, ((looking at viewer))',
    #     'extra_prompts': []
    # },
    # 'foursome_blowjob_cum_on_face': {
    #     'type': 'action',
    #     'poses': [
    #         # Вариант 1 — классический POV сверху
    #         '(3girls):1.7, side-by-side, squatting down and leaning forward, looking at viewer, '
    #         'triple blowjob, cooperative fellatio, teamwork, licking dick,, '
    #         'one girl grabbing testicles, petting head, '
    #         'erection pov, from above, (1man, man out of frame), '
    #         'huge cumshot, projectile cum, cum on faces:1.2, dripping cum, messy cum, '
    #         'flushed cheeks, vulnerable gasp, lustful expressions',
    #         # Вариант 2 — акцент на лица
    #         '(3girls):1.7, kneeling close together, intimate grouping, '
    #         'triple blowjob, licking shaft and head, lips open, tongues out, '
    #         'pov angle focused on faces, cumshot impact on cheeks, dripping cum, '
    #         'cooperative teamwork, shared attention, '
    #         'flushed cheeks, gasping, playful lustful eyes',
    #         # Вариант 3 — акцент на акт и тестикулы
    #         '(3girls):1.7, side-by-side, leaning forward, '
    #         'two girls sucking shaft, third girl licking tip and grabbing testicles, '
    #         'erection pov, viewer perspective, '
    #         'huge cumshot, projectile cum, cumshot across faces and lips, '
    #         'cooperative fellatio, teamwork, '
    #         'open mouths, dripping semen, lustful gaze upward',
    #         # Вариант 4 — более "грязный" и экстремальный
    #         '(3girls):1.7, close-packed, kneeling in front of viewer, '
    #         'triple blowjob, tongues overlapping, saliva dripping, '
    #         'man out of frame, erection pov, '
    #         'explosive cumshot, projectile cum, faces covered in cum, '
    #         'cum bubbling, dripping from chins, messy group fellatio, '
    #         'flushed cheeks, lustful cooperation, overwhelmed expressions',
    #     ],
    #     'view_angles': [
    #         'pov angle from above, lower body focus',
    #         'intimate knee-level shot, focus on faces and mouths',
    #         'side perspective, emphasis on teamwork and shared attention',
    #         '(facial cum focus:1.3), zoomed on dripping cum and lustful expressions',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'titjob, paizuri, ((multiple penis))',
    #     'extra_prompts': []
    # },
    # 'twins_doggy_cum_on_body': {
    #     'type': 'action',
    #     'poses': [
    #         '(2girls, sisters, hetero), feet, toes, from_behind, side-by-side, pov, from above, testicles, ((1man, man out of frame)), (on all fours, perfect shape asses):1.9, ass grab, buttjob, small anus, presenting ass, cum on ass:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectile cum)), first girl smile, second girl close eyes and open mouth, (first girl cum on hair and back):1.2, (second girl cum on back and ass):1.2, ',
    #         '(2girls, sisters, hetero), feet, toes, from_behind, side-by-side, pov, from above, testicles, ((1man, man out of frame)), (on all fours, perfect shape asses):1.9, ass grab, buttjob, small anus, presenting ass, cum on ass:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectile cum)), first girl smile, second girl close eyes and open mouth, (first girl cum on hair and back):1.2, (second girl cum on back and ass):1.2, '
    #     ],
    #     'view_angles': [
    #         '(extreme close-up:1.7), intimate focus on lower back and hip connection, skin texture detailed',
    #         '(motion capture:1.6), dynamic movement suggestion, hair flowing, energy and rhythm emphasis',
    #         '(reflective surfaces:1.5), dual angle intimacy'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': 'vulnerable gasp, flushed cheeks',
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on ass, titjob, paizuri, multiple penis, identity censor, ((looking at viewer))',
    #     'extra_prompts': []
    # },
    # 'twins_blowjob': {
    #     'type': 'action',
    #     'poses': [
    #         '(2girls, twins), side-by-side, teamwork, cooperative fellatio, saliva, pov, blowjobsandwich, penis between mouths, looking at viewer, erection pov, from above, ((1man, man out of frame)), testicles, small penis:1.8, petting head, squatting down and leaning forward, one girl grabbing testicles, double blowjob, licking dick',
    #         '(2girls, twins), side-by-side, teamwork, cooperative fellatio, saliva, pov, blowjobsandwich, penis between mouths, looking at viewer, erection pov, from above, ((1man, man out of frame)), testicles, small penis:1.8, petting head, squatting down and leaning forward, one girl grabbing testicles, double blowjob, licking dick'
    #     ],
    #     'view_angles': [
    #         '(whispering proximity:1.4), intimate distance emphasizing lips and neck',
    #         '(intimate chiaroscuro:1.5), dramatic lighting on upper body, deep shadows',
    #         '(soft focus intimacy:1.4), dreamy atmosphere, sharp upper body details'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on ass, titjob, paizuri, multiple penis, deformed fingers, chromatic aberration, identity censor',
    #     'extra_prompts': []
    # },
    # 'twins_blowjob_cum_on_face': {
    #     'type': 'action',
    #     'poses': [
    #         # Вариант 1 — классический POV сверху
    #         '(2girls):1.7, side-by-side, squatting down and leaning forward, looking at viewer, '
    #         'cooperative fellatio, teamwork, licking dick,, '
    #         'one girl grabbing testicles, petting head, '
    #         'erection pov, from above, '
    #         'huge cumshot, projectile cum, cum on faces:1.2, dripping cum, messy cum, '
    #         'flushed cheeks, vulnerable gasp, lustful expressions',
    #         # Вариант 2 — акцент на лица
    #         '(2girls):1.7, kneeling close together, intimate grouping, '
    #         'licking shaft and head, lips open, tongues out, '
    #         'pov angle focused on faces, cumshot impact on cheeks, dripping cum, '
    #         'cooperative teamwork, shared attention, '
    #         'flushed cheeks, gasping, playful lustful eyes',
    #         # Вариант 3 — акцент на акт и тестикулы
    #         '(2girls):1.7, side-by-side, leaning forward, '
    #         'two girls sucking shaft, '
    #         'erection pov, viewer perspective, '
    #         'huge cumshot, projectile cum, cumshot across faces and lips, '
    #         'cooperative fellatio, teamwork, '
    #         'open mouths, dripping semen, lustful gaze upward',
    #         # Вариант 4 — более "грязный" и экстремальный
    #         '(2girls):1.7, close-packed, kneeling in front of viewer, '
    #         'tongues overlapping, saliva dripping, '
    #         'erection pov, '
    #         'explosive cumshot, projectile cum, faces covered in cum, '
    #         'cum bubbling, dripping from chins, messy group fellatio, '
    #         'flushed cheeks, lustful cooperation, overwhelmed expressions',
    #     ],
    #     'view_angles': [
    #         '(intimate close-up), pov angle from above, lower body focus',
    #         '(kneeling close-up:1.5), intimate knee-level shot, focus on faces and mouths',
    #         '(seated intimacy:1.4), side perspective, emphasis on teamwork and shared attention',
    #         '(facial cum focus:1.3), zoomed on dripping cum and lustful expressions',
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on ass, titjob, paizuri, multiple penis, deformed fingers, chromatic aberration, identity censor',
    #     'extra_prompts': []
    # },
    # 'twins_blowjob_cum_in_mouth': {
    #     'type': 'action',
    #     'poses': [
    #         '(2girls, sisters, hetero), side-by-side, teamwork, cooperative fellatio, saliva, pov, blowjobsandwich, looking at viewer, erection pov, from above, ((1man, man out of frame)), testicles, squatting down and leaning forward, cum in mouth:1.4, cum on faces:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectiles cum)), small penis:1.8, petting head, first girl smile and open mouth, second girl close eyes and open mouth',
    #         '(2girls, sisters, hetero), side-by-side, teamwork, cooperative fellatio, saliva, pov, blowjobsandwich, looking at viewer, erection pov, from above, ((1man, man out of frame)), testicles, squatting down and leaning forward, cum in mouth:1.4, cum on faces:1.2, huge cumshot, cum bubbling, lot of cum, cumshot, ((projectiles cum)), small penis:1.8, petting head, first girl smile and open mouth, second girl close eyes and open mouth'
    #     ],
    #     'view_angles': [
    #         '(close upper body:1.5), intimate crop from waist up, detailed fabric textures',
    #         '(intimate eye-level closeness:1.4), proximity emphasizing facial features and upper torso',
    #         '(intimate undressing:1.5), hands pulling fabric, upper body tension visible'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': 'vulnerable gasp, flushed cheeks',
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on ass, titjob, paizuri, multiple penis, deformed fingers, chromatic aberration, identity censor',
    #     'extra_prompts': []
    # },
    # 'twins_blowjob_cum_play': {
    #     'type': 'action',
    #     'poses': [
    #         '(2girls, sisters, hetero), side-by-side, teamwork, looking at viewer, from above, squatting down and leaning forward, cum in mouth:1.2, cum bubbling, lot of cum, first girl open mouth dripping cum between lips, second girl close eyes and open mouth dripping cum between lips, tongues touching, mouths slick and parted, (cum swap:1.4), dripping cum between lips, soft flushed cheeks, girls kisses',
    #         '(2girls, sisters, hetero), side-by-side, teamwork, looking at viewer, from above, squatting down and leaning forward, cum in mouth:1.2, cum bubbling, lot of cum, first girl open mouth dripping cum between lips, second girl close eyes and open mouth dripping cum between lips, tongues touching, mouths slick and parted, (cum swap:1.4), dripping cum between lips, soft flushed cheeks, girls kisses'
    #     ],
    #     'view_angles': [
    #         '(close upper body:1.5), intimate crop from waist up, detailed fabric textures',
    #         '(intimate eye-level closeness:1.4), proximity emphasizing facial features and upper torso',
    #         '(intimate undressing:1.5), hands pulling fabric, upper body tension visible'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'cum on ass, titjob, paizuri, multiple penis, deformed fingers, chromatic aberration, identity censor',
    #     'extra_prompts': []
    # },
    # 'mob_wins_ass_licking': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, standing:1.5, nude, (perfect ass, perky ass, bubblebutt):1.6, (innie pussy, dripping pussy, smooth pussy, cameltoe):1.9, grabbing her ass, spreading her ass cheeks, bent over, slutty smile, thick pussy lips',
    #         '1girl, standing:1.5, nude, (perfect ass, perky ass, bubblebutt):1.6, (innie pussy, dripping pussy, smooth pussy, cameltoe):1.9, grabbing her ass, spreading her ass cheeks, bent over, slutty smile, thick pussy lips'
    #     ],
    #     'view_angles': [
    #         '(intimate low angle:1.5), from floor level emphasizing legs and hips, sensual perspective',
    #         '(lower body focus:1.4), crop from waist down, detailed fabric textures and contours',
    #         '(legs emphasis:1.5), full leg length visible, elegant leg lines, intimate framing',
    #         '(dynamic motion blur:1.5), intimate movement capture, slight motion suggestion, sensual energy flow',
    #         '(overhead perspective:1.6), intimate top-down view, emphasizing full body positioning, compositional balance'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'multiple people:1.9, crowd, extra figures, additional characters:1.9, (facing away, back to viewer, from behind, side view, profile, looking away):2.0, bra, shirt, distant view, windowed view',
    #     'extra_prompts': []
    # },
    # 'mob_wins_pussy_licking': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, nude, on back, front view, (legs spread open):1.5, knees out, looking at viewer,  intimate closeness, no background distraction, very tight asshole, asshole visible',
    #         '1girl, nude, on back, front view, (legs spread open):1.5, knees out, looking at viewer,  intimate closeness, no background distraction, very tight asshole, asshole visible'
    #     ],
    #     'view_angles': [
    #         '(three-quarter intimacy:1.5), diagonal angle, highlighting hip curvature and thigh lines, artistic composition',
    #         '(extreme proximity:1.7), intimate closeness, no background distraction, focused on skin and form'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': '2heads',
    #     'extra_prompts': []
    # },
    # 'mob_wins_face_sitting': {
    #     'type': 'action',
    #     'poses': [
    #         '((1girl)), standing tall, nude, looking down at viewer, (ultra low angle:1.9), from lying viewer perspective, legs wide apart:1.8, (legs spread wide open):1.9, (((pussy close-up))), <lora:midis_CunnilingusPov_V0.61[IL]:0.5>, looking down, smile, mouth open',
    #         '1girl, standing tall, nude, looking down at viewer, (ultra low angle:1.9), from lying viewer perspective, legs wide apart:1.8, (legs spread wide open):1.9, (((pussy close-up))), <lora:midis_CunnilingusPov_V0.61[IL]:0.5>, looking down, smile, mouth open'
    #     ],
    #     'view_angles': [
    #         '(POV:1.6), lying on floor looking up, low angle view of partner standing over, vulnerable perspective, eye contact from below, soft lighting(POV:1.6), lying on floor looking up, low angle view, ceiling perspective, intimate upward gaze',
    #         '(POV from ground:1.5), floor level perspective, looking upward, supine position, immersive low-angle view'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'naked_bottom',
    #     'negative_prompt': '((tongue out)), tongue, grass',
    #     'extra_prompts': []
    # },
    # 'missionary_vaginal': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, close up, foreshortening, glossy body, narrow waist, lying on back, penis in pussy:1.8, ',
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, close up, foreshortening, glossy body, narrow waist, lying on back, penis in pussy:1.8, '
    #     ],
    #     'view_angles': [
    #         '(cinematic close-up:1.7), waist-down focus, intimate crop, shallow depth of field, skin texture detailed',
    #         '(dramatic lighting:1.6), chiaroscuro effect, intimate shadows and highlights, rim light on curves'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum, cumshot, cum on face, cum on belly, (((penis in ass)))',
    #     'extra_prompts': []
    # },
    # 'missionary_anal': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, grabbing own knees, from above, high angle shot, fear emotion, close up, foreshortening, glossy body, narrow waist, lying on back, face twisted in unbearable agony, screaming mouth, penis in ass:1.9',
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, grabbing own knees, from above, high angle shot, fear emotion, close up, foreshortening, glossy body, narrow waist, lying on back, face twisted in unbearable agony, screaming mouth, penis in ass:1.9'
    #     ],
    #     'view_angles': [
    #         'bold outlines, dramatic perspective, comic book artistry',
    #         '(close ass:1.4), intimate sex perspective, exaggerated proportions, vibrant colors'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum, cumshot, cum on face, cum on belly, (((penis in pussy)))',
    #     'extra_prompts': []
    # },
    # 'missionary_cum_on_body': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, smile, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, pov from above, cum on belly:1.2, cumshot, projectile cum, wide angle, pov crotch, pov penis, suddenly, POV erection, cum on breasts:1.2, huge cumshot, cum bubbling, grabbing own breasts',
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, smile, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, pov from above, cum on belly:1.2, cumshot, projectile cum, wide angle, suddenly, cum on breasts:1.2, huge cumshot, cum bubbling, grabbing own breasts'
    #     ],
    #     'view_angles': [
    #         'modern aesthetic, clean lines, minimalist intimacy, artistic subtlety',
    #         'soft color bleeding, transparent layers, delicate wash effects',
    #         'visible brush strokes, impasto technique, rich color depth'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together',
    #     'extra_prompts': []
    # },
    # 'missionary_cum_in_pussy': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, smile, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, pov from above, cum in pussy:1.2, wide angle, pov crotch, pov penis, suddenly, POV erection, cum bubbling, grabbing own breasts, penis in pussy, pussy creampie, rolling eyes, еcstasy, overflow:1.5',
    #         '1girl, 1boy, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, smile, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, cum in pussy:1.2, wide angle, suddenly, cum bubbling, grabbing own breasts, penis in pussy, pussy creampie, rolling eyes, еcstasy, overflow:1.5'
    #     ],
    #     'view_angles': [
    #         'brushstroke effect, light play, sensual color blending, artistic interpretation',
    #         'classical proportions, balanced framing, titian-esque lighting'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together',
    #     'extra_prompts': []
    # },
    # 'missionary_cum_in_ass': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, cum in ass:1.2, wide angle, suddenly, cum bubbling, grabbing own breasts, penis in ass, ass creampie, rolling eyes, еcstasy, overflow:1.5, face twisted in unbearable agony, screaming mouth',
    #         '1girl, 1boy, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on back, front view, (legs spread apart), knees out, feet down, from above, high angle shot, close up, foreshortening, glossy body, narrow waist, good proportion body, best proportion body, lying on back, pov from above, cum in ass:1.2, wide angle, pov crotch, pov penis, suddenly, POV erection, cum bubbling, grabbing own breasts, penis in ass, ass creampie, rolling eyes, еcstasy, overflow:1.5, face twisted in unbearable agony, screaming mouth'
    #     ],
    #     'view_angles': [
    #         '(soft focus dreamscape:1.6), ethereal atmosphere, slightly blurred edges, romantic haze effect',
    #         'dramatic composition, rich shadows, classical painting style, old masters influence'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum on face, cum on belly, blowjob, handjob, titjob, cum in pussy, cum on pussy',
    #     'extra_prompts': []
    # },
    # 'doggy_vaginal': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, POV erection, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on all fours, front view, from above, high angle shot, close up, penis in pussy:1.9, deep penetration, hands on ass, spreding ass, presenting asshole, small anus, (small round asshole):1.5, narrow asshole',
    #         '1girl, 1boy, POV erection, presenting pussy:1.7, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on all fours, front view, from above, high angle shot, close up, penis in pussy:1.9, deep penetration, hands on ass, pov erection, pov spreding ass, presenting asshole, small anus, (small round asshole):1.5, narrow asshole'
    #     ],
    #     'view_angles': [
    #         '(dynamic low angle:1.6), from floor perspective, emphasizing curved back and raised hips, sensual upward view',
    #         '(cinematic rear view:1.7), intimate three-quarter angle, highlighting spine curvature and shoulder tension',
    #         '(dramatic backlighting:1.6), silhouette effect, rim light outlining curves, intimate shadows',
    #         '(over-shoulder intimacy:1.5), perspective from behind, capturing shoulder blades and back arch'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'strained pleasure, mixed with pain, biting lip',
    #         'abandoned restraint, wild expression, uncontrolled passion',
    #         'submissive ecstasy, completely dominated, willing surrender'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, (((penis in ass)))',
    #     'extra_prompts': []
    # },
    # 'doggy_anal': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, sexy pose, POV erection, eyes half open, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, penis in ass:1.9, deep penetration, face twisted in unbearable agony, screaming mouth, doggy style',
    #         '1girl, 1boy, sexy pose, POV erection, eyes half open, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, penis in ass:1.9, deep penetration, pov erection, face twisted in unbearable agony, screaming mouth, doggy style'
    #     ],
    #     'view_angles': [
    #         'naturalistic details, romantic lighting, waterhouse influence',
    #         'flat perspective, decorative patterns, traditional woodblock style',
    #         'concept art quality, magical lighting, greg rutkowski style',
    #         '(nocturnal intimacy:1.6), moonlight shadows, blue tones, mysterious night atmosphere',
    #         '(passionate intensity:1.7), warm golden light, dynamic energy, expressive composition'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'intense pleasure, ecstatic expression, overwhelmed by sensation',
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, (((penis in pussy))), sad, crying, angry, disgusted, painful, traumatic',
    #     'extra_prompts': []
    # },
    # 'doggy_cum_in_ass': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, sexy pose, eyes half open, POV erection, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, ((penis in ass)):1.9, deep penetration, pov erection, face twisted in unbearable agony, screaming mouth, doggy style, lot of cum, ass creampie, cum in ass:1.2, cum bubbling, overflow:1.5, full ass of cum, shy expression',
    #         '1girl, 1boy, sexy pose, eyes half open, POV erection, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, penis in ass:1.9, deep penetration, pov erection, face twisted in unbearable agony, screaming mouth, doggy style, lot of cum, ass creampie, cum in ass:1.2, cum bubbling, overflow:1.5, full ass of cum, shy expression'
    #     ],
    #     'view_angles': [
    #         'classical proportions, perfect anatomical study',
    #         'unexpected angles, magical realism, dreamlike perspective',
    #         'high contrast lighting, vintage cinematic atmosphere'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum on face, cum on belly, blowjob, handjob, titjob, cum in pussy, cum on pussy',
    #     'extra_prompts': []
    # },
    # 'doggy_cum_on_ass': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, POV erection, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, lot of cum, on all fours:1.6, high angle shot, foreshortening, pov erection, doggy style, smile, cum on ass:1.2, huge cumshot, cum bubbling, cumshot, projectile cum, cum on back:1.2, cum on buttocks:1.2, small anus, (small round asshole):1.5, narrow asshole',
    #         '1girl, 1boy, POV erection, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, lot of cum, on all fours:1.6, high angle shot, foreshortening, pov erection, doggy style, smile, cum on ass:1.2, huge cumshot, cum bubbling, cumshot, projectile cum, cum on back:1.2, cum on buttocks:1.2, small anus, (small round asshole):1.5, narrow asshole'
    #     ],
    #     'view_angles': [
    #         'classical proportions, perfect anatomical study',
    #         'unexpected angles, magical realism, dreamlike perspective',
    #         'high contrast lighting, vintage cinematic atmosphere'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum on face, cum on belly, blowjob, handjob, titjob, cum in pussy, cum on pussy',
    #     'extra_prompts': []
    # },
    # 'doggy_gapping_ass': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, sexy pose, eyes half open, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, cum in ass:1.8, (gaping anus):1.7, grabbing her ass, spreading her ass cheeks, spreading her butthole, anal creampie:1.5, smile expression, head on ground, cum bubbling, full asshole of cum, lot of cum',
    #         '1girl, sexy pose, eyes half open, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, foreshortening, cum in ass:1.8, (gaping anus):1.7, grabbing her ass, spreading her ass cheeks, spreading her butthole, anal creampie:1.5, smile expression, head on ground, cum bubbling, full asshole of cum, lot of cum'
    #     ],
    #     'view_angles': [
    #         '(dynamic perspective:1.6), slightly dutch angle, creating tension and movement',
    #         '(baroque elegance:1.7), rich drapery, luxurious fabrics, rubens-esque composition',
    #         '(contemporary art:1.6), clean lines, modern aesthetic, minimalist intimacy'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum on face, cum on belly, blowjob, handjob, titjob',
    #     'extra_prompts': []
    # },
    # 'doggy_cum_in_pussy': {
    #     'type': 'action',
    #     'poses': [
    #         '1girl, 1boy, POV erection, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, close up, foreshortening, penis in pussy:1.9, deep penetration, pov erection, doggy style, penis in pussy, pussy creampie, cum in pussy:1.2, cum bubbling, smile, small anus, (small round asshole):1.5, narrow asshole',
    #         '1girl, 1boy, POV erection, sexy pose, eyes half open, looking at viewer, wide ass, open ass, puffy pussy, on all fours:1.6, high angle shot, close up, foreshortening, penis in pussy:1.9, deep penetration, pov erection, doggy style, penis in pussy, pussy creampie, cum in pussy:1.2, cum bubbling, smile, small anus, (small round asshole):1.5, narrow asshole'
    #     ],
    #     'view_angles': [
    #         'diagonal framing, leading lines from heels to shoulders',
    #         'dramatic light and shadow play, caravaggio style intimacy',
    #         'intimate fabric details, stockings texture, skin pores visible'
    #     ],
    #     'variations': NUM_VARIATIONS,
    #     'emotion': [
    #         'shy embarrassment, blushing, modest covering',
    #         'forced compliance, worried eyes, resigned',
    #         'shy vulnerability, nervous, self-conscious',
    #         'awkward exposure, uncomfortable, hesitant',
    #         'submissive display, downward gaze, reluctant'
    #     ],
    #     'clothing_logic': 'full_naked',
    #     'negative_prompt': 'feet together, cum on face, cum on belly, blowjob, handjob, titjob, cum in ass, cum on ass',
    #     'extra_prompts': []
    # },
    'demonstration_naked_breasts': {
        'type': 'stage',
        'poses': [
            '1girl, hands under breasts, pushing up, completely topless, naked breasts, leaning forward',
            '1girl, arms crossed over chest, covering breasts, bare chest, no clothing, shy expression',
            '1girl, hands cupping breasts, presenting, fully exposed, nipples visible',
            '1girl, dress open, breasts revealed, hands holding breasts, bare shoulders'
        ],
        'view_angles': [
            'close-up, focus on breasts and hands, shallow depth of field',
            'low angle, from below, emphasizing curvature',
            'eye-level, direct view, capturing face and body',
        ],
        'clothing_logic': 'naked_top',
        'variations': NUM_VARIATIONS,
        'emotion': [
            'shy embarrassment, blushing, modest covering',
            'forced compliance, worried eyes, resigned',
            'shy vulnerability, nervous, self-conscious',
            'awkward exposure, uncomfortable, hesitant',
            'submissive display, downward gaze, reluctant'
        ],
        'extra_prompts': [
            'bust highlight, curved forms, soft skin',
            'intimate lighting, warm glow, gentle shadows',
            'reluctant body language, tense, nervous'
        ],
        'negative_prompt': "clothing, dress, top, bra, covered, fabric, wearing, strategically placed, (monitor:1.9), cum, cum on breasts"
    },
    'demonstration_naked_ass': {
        'type': 'stage',
        'poses': [
            "(completely naked ass:2.2), (bare butt:2.0), (no panties:2.0), "
            "(skirt lifted:2.0), (fully exposed:2.0), (nude lower body:2.0), "
            "(bare cheeks:2.0), (seductive smile:1.6), (flirtatious glance:1.5), "
            "(bent over:1.7), (looking back:1.6), (provocative pose:1.5)"
            "1girl, standing:1.5, nude, (perfect ass, perky ass, bubblebutt):1.6",
            "(completely naked ass:2.2), (bare butt:2.0), (no panties:2.0), "
            "(skirt lifted:2.0), (fully exposed:2.0), (nude lower body:2.0), "
            "(bare cheeks:2.0), (seductive smile:1.6), (flirtatious glance:1.5), "
            "(bent over:1.7), (looking back:1.6), (provocative pose:1.5)"
            "1girl, standing:1.5, nude, (perfect ass, perky ass, bubblebutt):1.6, hands on ass",
        ],
        'view_angles': [
            '(three-quarter intimacy:1.5), diagonal angle, highlighting hip curvature and thigh lines, artistic composition',
            '(extreme proximity:1.7), intimate closeness, no background distraction, focused on skin and form'
        ],
        'clothing_logic': 'naked_bottom',
        'variations': NUM_VARIATIONS,
        'emotion': [
            'shy embarrassment, blushing, modest covering',
            'forced compliance, worried eyes, resigned',
            'shy vulnerability, nervous, self-conscious',
            'awkward exposure, uncomfortable, hesitant',
            'submissive display, downward gaze, reluctant'
        ],
        'extra_prompts': [
            'curved forms, teasing lift',
            'warm glow, gentle shadows on curves',
            'tense shoulders, nervous hands',
        ],
        'negative_prompt': ("panties, underwear, bottom, clothing, dress, skirt, covered, "
                            "fabric, cloth, wearing, garment, strategically placed, (cum:1.8), (monitor:1.9)")
    },
    'farewell': {
        'type': 'stage',
        'poses': [
            '(graceful exit:1.3), 1girl, hand waving, portal framing curves',
            '(lingering goodbye:1.4), 1girl, looking back, hand on hip, soft smile',
            '(ethereal fade:1.3), 1girl, stepping through, dress fluttering, wistful eyes',
            '(teasing departure:1.4), 1girl, blowing kiss, body silhouetted in light',
            '(mystical vanish:1.3), 1girl, arms open, energy swirling around form'
        ],
        'view_angles': [
            '(back turn:1.3), over shoulder glance',
            '(front wave:1.4), facing with portal',
            '(side step:1.3), profile entering light',
            '(low fade:1.4), upward wistful',
            '(high depart:1.3), downward swirling'
        ],
        'emotion': ['wistful smile, lingering gaze',],
        'clothing_logic': 'full_dressed',
        'variations': NUM_VARIATIONS,
        'extra_prompts': [
            '(dimensional rift:1.2), sparkling vortex, soft pull'
        ],
        'negative_prompt': ''
    },
    'demonstration_panties': {
        'type': 'stage',
        'poses': [
            '(teasing lift:1.5), 1girl, standing, skirt pulled up with one hand, lace panties revealed, biting lip, playful eyes',
            '(provocative glance:1.4), 1girl, sitting, legs slightly apart, panties visible under lifted skirt, seductive smirk',
            '(alluring reveal:1.5), 1girl, lying on back, one knee bent, tugging panties slightly aside, mischievous look',
            '(panty tease:1.4), 1girl, standing sideways, thumbs hooking panties, pulling down slightly, bold grin',
            '(intimate sit:1.5), 1girl, sitting on floor, legs spread teasingly, panties glowing faintly, lustful gaze'
        ],
        'view_angles': [
            '(intimate low angle:1.5), shot from below skirt, emphasizing panty reveal',
            '(three-quarter tease:1.4), angled view, skirt lifted, panties highlighted',
            '(close-up focus:1.5), tight frame on panties and thighs, seductive glow',
            '(dynamic high angle:1.3), from above, looking down as she exposes lingerie'
        ],
        'clothing_logic': 'naked_bottom',
        'variations': NUM_VARIATIONS,
        'emotion': ['provocative teasing, mischievous glance, bold expression'],
        'extra_prompts': [
            '(intimate lingerie reveal:1.4), seductive panty showcase, playful aura',
            '(panty tease:1.3), subtle emphasis, alluring posture, erotic charm'
        ],
        'negative_prompt': ''
    },
    'demonstration_stockings': {
        'type': 'stage',
        'poses': [
            '(teasing adjustment:1.5), 1girl, sitting, one leg raised, hand sliding up stocking, playful smirk',
            '(seductive pull:1.4), 1girl, standing, tugging at garter strap, biting lip, confident gaze',
            '(alluring showcase:1.5), 1girl, lying on side, one hand stroking thigh, stockings shining, sultry eyes',
            '(provocative stretch:1.4), 1girl, standing tall, one leg extended forward, running hand along stocking',
            '(intimate sit:1.5), 1girl, kneeling, tugging stocking halfway down, mischievous grin'
        ],
        'view_angles': [
            '(low leg angle:1.5), from floor, focusing on stockings and thighs, seductive',
            '(three-quarter thigh view:1.4), angled shot highlighting garters and curves',
            '(close-up stockings:1.5), tight focus on hands sliding stockings, sensual glow',
            '(side profile leg tease:1.4), accentuating long legs and stocking detail'
        ],
        'clothing_logic': 'full_dressed',
        'variations': NUM_VARIATIONS,
        'emotion': ['teasing smile, seductive glance, playful allure, confident charm'],
        'extra_prompts': [
            '(stocking tease:1.4), smooth legs, sensual highlight',
            '(garter allure:1.3), lingerie accent'
        ],
        'negative_prompt': ''
    },
    'striptease': {
        'type': 'stage',
        'poses': [
            '(playful reveal:1.5), 1girl, standing, lifting dress slowly, showing underwear, teasing eyes',
            '(seductive undress:1.4), 1girl, tugging shirt off one shoulder, chest exposed partially, sultry smirk',
            '(intimate strip:1.5), 1girl, pulling panties aside, biting lip, mischievous glance',
            '(slow tease:1.4), 1girl, sitting on chair, sliding skirt down legs, confident expression',
            '(provocative peel:1.5), 1girl, hands raising top above chest, gaze down at viewer, bold grin'
        ],
        'view_angles': [
            '(intimate low angle:1.5), from below, emphasizing undressing and curves',
            '(three-quarter strip:1.4), angled view showing body mid-strip, teasing look',
            '(close-up undress:1.5), tight frame on hands removing clothes, erotic highlight',
            '(dynamic stage view:1.4), slightly offset, focusing on strip motion and posture'
        ],
        'clothing_logic': 'naked_top',
        'variations': NUM_VARIATIONS,
        'emotion': ['playful grin, bold smirk, sultry seduction, mischievous charm'],
        'extra_prompts': [
            '(seductive strip:1.4), clothes sliding off body, teasing exposure',
            '(slow reveal:1.3), fabric slipping, erotic allure, captivating tease'
        ],
        'negative_prompt': ''
    },
    'demonstration_love': {
        'type': 'stage',
        'poses': [
            '(tender embrace:1.5), 1girl, arms wrapping around self or air, soft smile, head tilted',
            '(playful affection:1.4), 1girl, hand to lips, coy glance, hips slightly swayed',
            '(intimate gaze:1.5), 1girl, leaning forward, eyes locking with viewer, soft smirk',
            '(sensual curl:1.4), 1girl, lying on side, hugging pillow or knee, relaxed yet erotic',
            '(gentle tease:1.5), 1girl, fingers brushing collarbone, inviting look, soft curves accentuated'
        ],
        'view_angles': [
            '(intimate front:1.5), close-up on face and upper body, soft lighting, tender gaze',
            '(three-quarter affectionate:1.4), angled view showing curves and inviting posture',
            '(low angle embrace:1.5), subtle erotic perspective emphasizing form',
            '(over-the-shoulder:1.4), gentle glance back, playful and loving expression'
        ],
        'clothing_logic': 'full_dressed',
        'variations': NUM_VARIATIONS,
        'emotion': ['soft, loving, teasing, intimate smile'],
        'extra_prompts': [
            '(tender allure:1.4), intimate pose, soft erotic charm',
            '(playful affection:1.3), inviting gaze, subtle sensuality'
        ],
        'negative_prompt': ''
    },
}

class TerminalElements():

    ACTIONS = ['DROP', 'FILTER', 'KEEP', 'SELL', 'TRADE', 'USE']

    CHECKBOXES = ['30 Sec God Mode', 'Auto AP', 'Auto Aggro', 'Auto Attack', 'Auto Buff', 'Auto Die', 'Auto Equip', 'Auto Exceed', 'Auto Feed', 'Auto HP', 'Auto Login', 'Auto Loot', 'Auto MP', 'Auto Mission', 'Auto NPC', 'Auto Pet', 'Auto Revive', 'Auto Rune', 'Auto SP', 'Buy Arrows', 'Buy HP Pot', 'Buy MP Pot', 'Buy Pet Food', 'Buy Return Scroll', 'Current location', 'Do not open Maple Guide on enter game', 'Do not open Mileage on enter game', 'Drop item at max per slot', 'EQUIP Rush', 'ETC Rush', 'Familiar 0', 'Familiar 1', 'Familiar 2', 'Flame Orb Hack', 'Full God Mode', 'Full Map Attack', 'General FMA', 'Grenade Kami', 'Guard God Mode', 'HP Pot Rush', 'Ignore Elite Monster', 'Ignore Skill Cooldown', 'Infinite Bullets', 'Instant Enchantment Scroll', 'Instant Enchantment Star', 'Instant Extraction', 'Instant Final Smash', 'Jump Down Anywhere', 'Kami Collision Items', 'Kami Loot', 'Kami Vac', 'La Mancha Spear Hack', 'Legit Vac', 'Lemmings', 'Logo Skipper', 'MP Pot Rush', 'Melee No Delay', 'Mob Disarm', 'Mob Falldown', 'Mob No Death Animation', 'Mob No Spawn Animation', 'Mob Speed Up', 'Mob Vac', 'MonkeySpiritsNDcheck', 'No Air Check', 'No Background', 'No Blazing Extinction Effect', 'No Blue Boxes', 'No Boss Map Effect', 'No Damage Info', 'No Delay Blazing Extinction', 'No Delay Flash Jump', 'No Fade Animation', 'No Fade Stages', 'No Knock Back', 'No Letter Box', 'No Login Error', 'No Loot Animation', 'No Map Object', 'No Rush', 'No Skill Effect', 'No Tile', 'No Weather', 'Npc Teleport [Tab]',
                  'Offline Mode', 'Pet Item Teleport', 'Portal Teleport [Back Space]', 'Remove Screen Clutter', 'Respond to GM Whisper', 'Rush By Level', 'Sell filter item', 'Sell hp/mp pots', 'Set item state as sell on first drop', 'Skill Injection', 'Skip Launcher', 'Slide And Attack', 'Spawn Control', 'Speedy Gonzales', 'Summon Kishin', 'Throw Blazing Extinction', 'USE Rush', 'Unlimited Vitality', 'Unlimtd Arrow Platter', 'Unlimtd Attack', 'Vellum Freeze', 'beastTamerModeCheck', 'bot/auto_die/bymob', 'bot/illium/radiant_javelin_delay', 'bot/illium/summon_control', 'bot/kanna_kami', 'bot/kishin_fma', 'bot/mercedes_hack', 'bot/portal_kami', 'bot/puffram', 'bot/si_no_wait', 'bot/summon_kami', 'bot/transfer/item', 'bot/transfer/keep_meso', 'bot/transfer/meso', 'charm_fma', 'dragon_kami', 'eliteCC', 'filter_all', 'filter_card', 'filter_equip', 'filter_etc', 'filter_familiar', 'filter_recipe', 'filter_setup', 'filter_use', 'flacc', 'macro1_check', 'macro2_check', 'macro3_check', 'macro4_check', 'macro5_check', 'main/boss_freeze', 'main/disable_quest_checks', 'main/filter_elite_monster', 'main/memory_reducer', 'main/mobnojump', 'main/nolag', 'map/maprusher/hypertelerock', 'mobvac_limit_check', 'ndmp', 'node_check', 'reset_inner', 'scanner/show_tooltip', 'settings/autoburn', 'settings/autochar', 'settings/block_quest_helper', 'settings/expcrash', 'settings/explogout', 'settings/loginwait', 'settings/mesocrash', 'settings/mesologout', 'settings/traveling_merchant', 'special/neb', 'timedCCCheck']

    LINEEIDTS = ['GMWhisperReset', 'LoginChar', 'LoginID', 'LoginPW', 'LoginSPW', 'MobVacX', 'MobVacY', 'SISkillID',
                 'ShopTitle', 'allowedChannels', 'bot/transfer/charid', 'bot/transfer/mapid', 'nextmapccportal', 'special/neb_exceptions']

    PUSHBUTTONS = ['Buy item', 'Drop item', 'Item filter',
                   'Leave shop', 'Recharge', 'Sell item', 'Use item']

    ADIOBUTTONS = ['MobVacChar', 'MobVacPos', 'SIRadioDragon', 'SIRadioMagic', 'SIRadioMelee', 'SIRadioShoot', 'SkillInjection1', 'SkillInjection2',
                   'bot/mobvac/new', 'bot/mobvac/old', 'bot/si_cadena', 'special/buy_cube_black', 'special/buy_cube_red', 'special/inner_legendary', 'special/inner_unique']

    SPINBOXES = ['Arrow', 'AutoDieExp', 'AutoDieLevel', 'FilterMeso', 'FlameBall', 'GMWhisper', 'HPPot', 'KamiLoot', 'KamiOffsetX', 'KamiOffsetY', 'MPPot', 'MonkeySpiritsNDdelay', 'PetFood', 'SkillInjection', 'autoattack_spin', 'autoloot_spin', 'bot/ballcount', 'bot/illium/radiant_javelin', 'bot/kami_delay', 'bot/kanna_kami_delay', 'bot/transfer/item_threshold',
                 'bot/transfer/keep_meso', 'bot/transfer/meso_threshold', 'charm_delay', 'inner_delay', 'macro1_spin', 'macro2_spin', 'macro3_spin', 'macro4_spin', 'macro5_spin', 'node_delay', 'settings/expcrash', 'settings/explogout', 'settings/loginwait1', 'settings/loginwait2', 'settings/loginwait3', 'settings/mesocrash', 'settings/mesologout', 'special/buy_cubes', 'timedCCSpin']
    
	SLIDERS = ['sliderHP', 'sliderMP']

    COMBOBOX = ['AttackKey', 'Familiar0', 'Familiar1', 'Familiar2', 'HPKey', 'HackingOpt', 'LoginChannel', 'LoginServer', 'LoginWorld', 'MPKey', 'beastTamerModeCombo',
                'bot/transfer/channelid', 'eva_cmb', 'macro1_combo', 'macro2_combo', 'macro3_combo', 'macro4_combo', 'macro5_combo', 'resolution', 'settings/autochar_job']

    def __init__(self):
        pass

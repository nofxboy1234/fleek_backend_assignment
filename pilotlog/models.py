from django.db import models


class Aircraft(models.Model):
    fin = models.CharField("Fin", max_length=50)
    sea = models.BooleanField("Sea", default=False)
    tmg = models.BooleanField("TMG", default=False)
    efis = models.BooleanField("Efis", default=False)
    fnpt = models.IntegerField("FNPT", default=0)
    make = models.CharField("Make", max_length=50)
    run2 = models.BooleanField("Run2", default=False)
    _class = models.IntegerField("Class", default=0)
    model = models.CharField("Model", max_length=50)
    power = models.IntegerField("Power", default=0)
    seats = models.IntegerField("Seats", default=0)
    active = models.BooleanField("Active", default=False)
    kg5700 = models.BooleanField("Kg5700", default=False)
    rating = models.CharField("Rating", max_length=50)
    company = models.CharField("Company", max_length=50)
    _complex = models.BooleanField("Complex", default=False)
    cond_log = models.IntegerField("CondLog", default=0)
    fav_list = models.BooleanField("FavList", default=False)
    category = models.IntegerField("Category", default=0)
    high_perf = models.BooleanField("HighPerf", default=False)
    sub_model = models.CharField("SubModel", max_length=50)
    aerobatic = models.BooleanField("Aerobatic", default=False)
    ref_search = models.CharField("RefSearch", max_length=50)
    reference = models.CharField("Reference", max_length=50)
    tailwheel = models.BooleanField("Tailwheel", default=False)
    default_app = models.IntegerField("DefaultApp", default=0)
    default_log = models.IntegerField("DefaultLog", default=0)
    default_ops = models.IntegerField("DefaultOps", default=0)
    device_code = models.IntegerField("DeviceCode", default=0)
    aircraft_code = models.CharField("AircraftCode", max_length=50, primary_key=True)
    default_launch = models.IntegerField("DefaultLaunch", default=0)
    record_modified = models.IntegerField("Record_Modified", default=0)

    @classmethod
    def get_verbose_names_to_fields(cls):
        verbose_name_fields = {}
        for verbose_name, field_name in map(
            lambda field: [field.verbose_name, field.name], cls._meta.fields
        ):
            verbose_name_fields[verbose_name] = str(field_name)

        return verbose_name_fields

    @classmethod
    def get_fields_to_verbose_names(cls):
        field_verbose_names = {}
        for field in cls._meta.fields:
            field_verbose_names[field.name] = str(field.verbose_name)

        return field_verbose_names

    def __str__(self):
        return self.aircraft_code


class Flight(models.Model):
    flight_code = models.CharField(
        max_length=255,
        primary_key=True,
        default="00000000-0000-0000-0000-000000011362",
        verbose_name="FlightCode",
    )
    pf = models.BooleanField(default=False, verbose_name="PF")
    pax = models.IntegerField(default=0, verbose_name="Pax")
    fuel = models.IntegerField(default=0, verbose_name="Fuel")
    de_ice = models.BooleanField(default=False, verbose_name="DeIce")
    route = models.CharField(max_length=255, default="", verbose_name="Route")
    to_day = models.IntegerField(default=0, verbose_name="ToDay")
    min_u1 = models.IntegerField(default=0, verbose_name="minU1")
    min_u2 = models.IntegerField(default=0, verbose_name="minU2")
    min_u3 = models.IntegerField(default=0, verbose_name="minU3")
    min_u4 = models.IntegerField(default=0, verbose_name="minU4")
    min_xc = models.IntegerField(default=136, verbose_name="minXC")
    arr_rwy = models.CharField(max_length=255, default="", verbose_name="ArrRwy")
    dep_rwy = models.CharField(max_length=255, default="", verbose_name="DepRwy")
    ldg_day = models.IntegerField(default=0, verbose_name="LdgDay")
    lift_sw = models.IntegerField(default=0, verbose_name="LiftSW")
    p1_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000000808",
        verbose_name="P1Code",
    )
    p2_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000000001",
        verbose_name="P2Code",
    )
    p3_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000000000",
        verbose_name="P3Code",
    )
    p4_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000000000",
        verbose_name="P4Code",
    )
    report = models.TextField(default="", verbose_name="Report")
    tag_ops = models.CharField(max_length=255, default="", verbose_name="TagOps")
    to_edit = models.BooleanField(default=False, verbose_name="ToEdit")
    min_air = models.IntegerField(default=0, verbose_name="minAIR")
    min_cop = models.IntegerField(default=136, verbose_name="minCOP")
    min_ifr = models.IntegerField(default=136, verbose_name="minIFR")
    min_imt = models.IntegerField(default=0, verbose_name="minIMT")
    min_pic = models.IntegerField(default=0, verbose_name="minPIC")
    min_rel = models.IntegerField(default=0, verbose_name="minREL")
    min_sfr = models.IntegerField(default=0, verbose_name="minSFR")
    arr_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000017531",
        verbose_name="ArrCode",
    )
    date_utc = models.DateField(default="2011-10-18", verbose_name="DateUTC")
    dep_code = models.CharField(
        max_length=255,
        default="00000000-0000-0000-0000-000000016665",
        verbose_name="DepCode",
    )
    hobbs_in = models.IntegerField(default=0, verbose_name="HobbsIn")
    holding = models.IntegerField(default=0, verbose_name="Holding")
    pairing = models.CharField(max_length=255, default="", verbose_name="Pairing")
    remarks = models.TextField(default="ILS24", verbose_name="Remarks")
    sign_box = models.IntegerField(default=0, verbose_name="SignBox")
    to_night = models.IntegerField(default=0, verbose_name="ToNight")
    user_num = models.IntegerField(default=0, verbose_name="UserNum")
    min_dual = models.IntegerField(default=0, verbose_name="minDUAL")
    min_exam = models.IntegerField(default=0, verbose_name="minEXAM")
    crew_list = models.TextField(default="", verbose_name="CrewList")
    date_base = models.DateField(default="2011-10-18", verbose_name="DateBASE")
    fuel_used = models.IntegerField(default=0, verbose_name="FuelUsed")
    hobbs_out = models.IntegerField(default=0, verbose_name="HobbsOut")
    ldg_night = models.IntegerField(default=0, verbose_name="LdgNight")
    next_page = models.BooleanField(default=False, verbose_name="NextPage")
    tag_delay = models.CharField(max_length=255, default="", verbose_name="TagDelay")
    training = models.TextField(default="", verbose_name="Training")
    user_bool = models.BooleanField(default=False, verbose_name="UserBool")
    user_text = models.TextField(default="", verbose_name="UserText")
    min_instr = models.IntegerField(default=0, verbose_name="minINSTR")
    min_night = models.IntegerField(default=136, verbose_name="minNIGHT")
    min_picus = models.IntegerField(default=0, verbose_name="minPICUS")
    min_total = models.IntegerField(default=136, verbose_name="minTOTAL")
    arr_offset = models.IntegerField(default=120, verbose_name="ArrOffset")
    date_local = models.DateField(default="2011-10-18", verbose_name="DateLOCAL")
    dep_offset = models.IntegerField(default=120, verbose_name="DepOffset")
    tag_launch = models.CharField(max_length=255, default="", verbose_name="TagLaunch")
    tag_lesson = models.CharField(max_length=255, default="", verbose_name="TagLesson")
    to_time_utc = models.IntegerField(default=0, verbose_name="ToTimeUTC")
    arr_time_utc = models.IntegerField(default=1296, verbose_name="ArrTimeUTC")
    base_offset = models.IntegerField(default=120, verbose_name="BaseOffset")
    dep_time_utc = models.IntegerField(default=1160, verbose_name="DepTimeUTC")
    ldg_time_utc = models.IntegerField(default=0, verbose_name="LdgTimeUTC")
    fuel_planned = models.IntegerField(default=0, verbose_name="FuelPlanned")
    next_summary = models.BooleanField(default=False, verbose_name="NextSummary")
    tag_approach = models.CharField(
        max_length=255, default="401", verbose_name="TagApproach"
    )
    aircraft_code = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        db_column="aircraft_code",
        verbose_name="AircraftCode",
        related_name="flights",
    )
    arr_time_sched = models.IntegerField(default=0, verbose_name="ArrTimeSCHED")
    dep_time_sched = models.IntegerField(default=0, verbose_name="DepTimeSCHED")
    flight_number = models.CharField(
        max_length=255, default="2706", verbose_name="FlightNumber"
    )
    flight_search = models.CharField(
        max_length=255, default="20111018:2706BCNPRG", verbose_name="FlightSearch"
    )
    record_modified = models.IntegerField(
        default=1616320991, verbose_name="Record_Modified"
    )

    @classmethod
    def get_verbose_names_to_fields(cls):
        verbose_name_fields = {}
        for verbose_name, field_name in map(
            lambda field: [field.verbose_name, field.name], cls._meta.fields
        ):
            verbose_name_fields[verbose_name] = str(field_name)

        return verbose_name_fields

    @classmethod
    def get_fields_to_verbose_names(cls):
        field_verbose_names = {}
        for field in cls._meta.fields:
            field_verbose_names[field.name] = str(field.verbose_name)

        return field_verbose_names

    def __str__(self):
        return self.flight_number

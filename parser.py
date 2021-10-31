class competition(lineup):
    def __init__(self, json_file):
        self.file = open(json_file, "r")
        self.data = self.file.read().strip().split("\n")
        self.competitions = {"competition_id":[],"season_id":[],"country_name":[],"competition_gender":[],"competition_youth":[],"competition_international":[],"season_name":[],"match_updated":[],"match_updated_360":[],"match_available_360":[],"match_available":[]}
    def parser(self):
        columns = ["competition_id","season_id","country_name","competition_gender","competition_youth","competition_international","season_name","match_updated","match_updated_360","match_available_360","match_available"]
        for row in self.data:
            row_as_list = row.split("\"")
            if len(row_as_list) >= 3:
                if row_as_list[1] in columns:
                    if row_as_list[1] in columns[0:2]:
                        self.competitions[row_as_list[1]].append(self.num_string_cleanup(row_as_list[2]))
                    elif row_as_list[1] in columns[2:4] or row_as_list[1] in columns[6:9] or row_as_list[1] == columns[-1]:
                        self.competitions[row_as_list[1]].append(row_as_list[3])
                    elif row_as_list[1] in columns[4:6]:
                        self.competitions[row_as_list[1]].append(self.true_false_cleanup(row_as_list[2]))
                    elif row_as_list[1] == 'match_available_360':
                        self.competitions[row_as_list[1]].append(self.null_check(row_as_list[2]))
                    else:
                        return "error"
        return self.competitions
    def true_false_cleanup(self, string):
        if string == ' : false,':
            return "false"
        elif string == ' : true,':
            return "true"
        else:
            return None
    def num_string_cleanup(self, string):
        number_string_list = ["0","1","2","3","4","5","6","7","8","9"]
        value = ""
        for i in range(len(string)):
            if string[i] in number_string_list:
                value += string[i]
        return int(value)
    def null_check(self,string):
        if string == " : null,":
            return None
        return string
class lineup(competition):
    def __init__(self, json_file):
        super().__init__(json_file)
        self.lineups = {"team_id":[],"team_name":[],"lineup":{"player_id":[],"player_name":[],"player_nickname":[],"jersey_number":[],"country_id":[],"country_name":[]}}
        
    def parser(self):
        for row in self.data:
            row_as_list = row.split("\"")
            if len(row_as_list) >= 3:
                if row_as_list[1] == 'team_id':
                    self.lineups["team_id"].append(self.num_string_cleanup(row_as_list[2]))
                elif row_as_list[1] == 'team_name':
                    self.lineups["team_name"].append(row_as_list[3])
                elif row_as_list[1] == 'player_id':
                    self.lineups['lineup']['player_id'].append(self.num_string_cleanup(row_as_list[2]))
                elif row_as_list[1] == 'player_name':
                    self.lineups['lineup']['player_name'].append(row_as_list[3])
                elif row_as_list[1] == 'player_nickname':
                    self.lineups['lineup']['player_nickname'].append(self.null_check(row_as_list[2]))
                elif row_as_list[1] == 'jersey_number':
                    self.lineups['lineup']['jersey_number'].append(self.num_string_cleanup(row_as_list[2]))
                elif row_as_list[1] == 'id':
                    self.lineups['lineup']['country_id'].append(self.num_string_cleanup(row_as_list[2]))
                elif row_as_list[1] == 'name':
                    self.lineups['lineup']['country_name'].append(row_as_list[3])
                else:
                    return "error"
        return self.lineups

# def main(argv):
#     if len(argv) < 2:
#         print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
#         sys.exit(1)
#     # loops over all .json files in the argument
#     for f in argv[1:]:
#         if isJson(f):
#             parseJson(f)
#             print ("Success parsing " + f) 

# if __name__ == '__main__':
#     main(sys.argv)

#python skeleton_parser_v2.py ebay_data/items-*.json
class match(competition): #This class is not working and under construction 👷‍♂️
    def __init__(self, json_file):
        super().__init__(json_file)
        self.matches = [{"match_id","match_id","kick_off","competition","season","home_team","away_team","home_score","away_score","match_status","match_status_360","last_updated","last_updated_360","metadata","match_week","competition_stage","stadium","referee"}]
        self.matches[0]["competition"] = {"competition_id","country_name","competition_name"}
        self.matches[0]["season"] = {"season_id","season_name"}
        self.matches[0]["home_team"] = {"home_team_id","home_team_name","home_team_gender","home_team_group","country","managers"}
        self.matches[0]["home_team"]["country"] = {"id","name"}
        self.matches[0]["home_team"]["managers"] = [{"id","name","nickname","dob","country"}]
        self.matches[0]["home_team"]["managers"][0]["country"]={"id","name"}
        self.matches[0]["away_team"] = {"away_team_id","away_team_name","away_team_gender","away_team_group","country","managers"}
        self.matches[0]["away_team"]["country"] = {"id","name"}
        self.matches[0]["away_team"]["managers"] = [{"id","name","nickname","dob","country"}]
        self.matches[0]["away_team"]["managers"][0]["country"]={"id","name"}
        self.matches[0]["metadata"] = {"data_version","shot_fidelity_version"}
        self.matches[0]["competition_stage"] = {"id","name"}
        self.matches[0]["stadium"] = {"id","name","country"}
        self.matches[0]["stadium"]["country"] = {"id","name"}
        self.matches[0]["referee"]= {"id","name","country"}
        self.matches[0]["referee"]["country"]={"id","name"}
        
                         
    def parser(self):
        for row in self.data:
            self.matches.append(self.matches[0])
            row_as_list = row.split("\"")
            return self.matches

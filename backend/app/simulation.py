from .network import DATA,G,get_node
def label(s):return 'SEVERE' if s>=85 else 'HIGH' if s>=65 else 'MODERATE' if s>=40 else 'LIMITED'
def simulate(asset_id,severity,duration_hours):
 o=get_node(asset_id)
 if not o:raise ValueError('Unknown asset')
 seen={asset_id};q=[(x,1) for x in G.neighbors(asset_id)];path=[asset_id]
 while q:
  x,depth=q.pop(0)
  if x in seen:continue
  seen.add(x);n=get_node(x);pressure=severity*(1-depth*.12)+duration_hours*1.5
  if pressure>=42+depth*9:
   path.append(x)
   if depth<3:q += [(y,depth+1) for y in G.neighbors(x) if y not in seen]
 path=path[:9]
 ns=[get_node(x) for x in path];services=[n for n in ns if n['service']];people=sum(n['population'] for n in ns)
 impact=round(min(99,25+severity*.48+duration_hours*1.2+len(path)*2.3));conf=round(max(72,96-duration_hours*.4-(100-severity)*.08))
 if o['criticality']>=85:action=f'Protect {o["name"]} and activate alternate route or redundant capacity.';reason='High systemic criticality makes dependency concentration a priority for immediate mitigation.';red=min(72,round(24+o['criticality']*.35));priority='IMMEDIATE'
 else:action=f'Inspect {o["name"]} and divert demand through the least-loaded alternative connection.';reason='Early intervention can reduce downstream stress before the disruption compounds.';red=min(60,round(18+o['criticality']*.28));priority='HIGH'
 return {'origin_name':o['name'],'severity':severity,'duration_hours':duration_hours,'severity_label':label(severity),'impact_score':impact,'assets_affected':len(path),'people_affected':people,'confidence':conf,'cascade_path':[get_node(x)['name'] for x in path],'services':[{'name':n['name'],'status':'EXPOSED' if severity>=65 else 'AT RISK'} for n in services[:5]] or [{'name':'No critical service in cascade','status':'MONITOR'}],'effects':[{'label':'NETWORK CONNECTIVITY','value':f'-{min(68,8+len(path)*4)}%'},{'label':'TRAVEL PRESSURE','value':f'+{min(95,12+severity//2+duration_hours*2)}%'},{'label':'SERVICE EXPOSURE','value':f'{min(88,18+len(services)*15)}%'},{'label':'RECOVERY WINDOW','value':f'{max(2,duration_hours+len(path)//2)} h'}],'recommendation':{'action':action,'reason':reason,'risk_reduction':red,'priority':priority}}
def warnings():
 a=[('Central Junction','Traffic load','+31% deviation'),('Power Substation A','Thermal load','+18% deviation'),('River Bridge Alpha','Structural signal','-14% margin'),('North Arterial','Travel time','+27% deviation')]
 return [{'asset_name':x,'signal':s,'deviation':v,'status':'REVIEW REQUIRED'} for x,s,v in a]
def interventions():
 out=[]
 for n in sorted(DATA['nodes'],key=lambda x:x['criticality'],reverse=True)[:6]:
  r=min(68,max(18,round(n['criticality']*.52)));out.append({'asset_name':n['name'],'action':'Reduce dependency concentration; validate alternate capacity.','risk_reduction':r,'priority':'IMMEDIATE' if r>=45 else 'HIGH'})
 return out

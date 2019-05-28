
        if op.type == 32:
            if op.param3 in Zmid:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)                                     
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    X = kf.getGroup(op.param1)
                    kf.updateGroup(X)
                    X.preventedJoinByTicket = True
                    kf.inviteIntoGroup(op.param1,[Zmid])
                    wait["blacklist"][op.param2] = True
                else:
                    pass

        if op.type == 32:
            if op.param3 in Jmid:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)                                     
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)                                     
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    X = kf.getGroup(op.param1)
                    kf.updateGroup(X)
                    X.preventedJoinByTicket = True
                    kf.inviteIntoGroup(op.param1,[Jmid])
                    wait["blacklist"][op.param2] = True
                else:
                    pass
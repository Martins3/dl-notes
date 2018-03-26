`timescale 1ns / 1ps


module ez(
    input flag,
    output out,
    output q1,
    output q2,
    output q3,
    output q4
    );
    wire out;
    reg q1=0;
    reg q2=0;
    reg q3=0;
    reg q4=0;







    always @(negedge flag)
    begin
    q1 <= ~q1;
    end;
    // up side or the down side
    always @(negedge q1)
    begin
    q2 <= (~q2)&(~q4);
    q4 <= (~q4)&(q2&q3);
    end;

    always @(negedge q2)
    begin
    q3 <= (~q3);
    end;


    assign out = (q1&q4)&flag;

endmodule



`timescale 1ns / 1ps


module ez(
    input flag,
    output out,
    output q1,
    output q2,
    output q3,
    output q4
    );
    wire out;
    reg q1=0;
    reg q2=0;
    reg q3=0;
    reg q4=0;




    


    always @(negedge flag)
    begin
    q1 <= ~q1;
    end;
    // up side or the down side
    always @(negedge q1)
    begin
    q2 <= (~q2)&(~q4);
    q4 <= (~q4)&(q2&q3);
    end;

    always @(negedge q2)
    begin
    q3 <= (~q3);
    end;


    assign out = (q1&q4)&flag;

endmodule

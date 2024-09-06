module tb_toplevel;

wire [9:0] LEDR;
reg [9:0] SW;
reg [3:0] KEY;
wire [6:0] HEX0;
reg [6:0] HEX1;
reg [6:0] HEX2;
reg [6:0] HEX3;
reg [6:0] HEX4;
reg [6:0] HEX5;
reg CLOCK_50;
reg RESET_N;

initial begin
    $from_myhdl(
        SW,
        KEY,
        HEX1,
        HEX2,
        HEX3,
        HEX4,
        HEX5,
        CLOCK_50,
        RESET_N
    );
    $to_myhdl(
        LEDR,
        HEX0
    );
end

toplevel dut(
    LEDR,
    SW,
    KEY,
    HEX0,
    HEX1,
    HEX2,
    HEX3,
    HEX4,
    HEX5,
    CLOCK_50,
    RESET_N
);

endmodule
